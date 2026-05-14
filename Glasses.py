import torch
import torch.nn as nn
from models.backbone.adapter2 import DINOv3_Adapter
import torch.nn.functional as F


class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3):
        super().__init__()
        padding = kernel_size // 2
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size, padding=padding, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.conv(x)


class ConvDown(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.conv(x)


class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels, mid_channels=None):
        super().__init__()
        if mid_channels is None:
            mid_channels = out_channels
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.conv(x)


class Attention(nn.Module):
    def __init__(self, dim, num_heads=8, qkv_bias=False, attn_drop=0., proj_drop=0.):
        super().__init__()
        assert dim % num_heads == 0, 'dim should be divisible by num_heads'
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = head_dim ** -0.5
        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)

        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)

    def forward(self, x):
        B, N, C = x.shape
        qkv = self.qkv(x).reshape(B, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]

        x_attn = F.scaled_dot_product_attention(
            q, k, v,
            dropout_p=self.attn_drop.p if self.training else 0.
        )
        x_attn = x_attn.transpose(1, 2).reshape(B, N, C)

        x = self.proj(x_attn)
        x = self.proj_drop(x)
        return x


class Mlp(nn.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None, drop=0.):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features

        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = nn.GELU()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)
        return x


class TransformerBlock(nn.Module):
    def __init__(self, dim, num_heads, mlp_ratio=4., qkv_bias=False, drop=0., attn_drop=0., drop_path=0.):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)

        self.attn = Attention(
            dim, num_heads=num_heads, qkv_bias=qkv_bias, attn_drop=attn_drop, proj_drop=drop
        )

        self.drop_path = nn.Dropout(drop_path) if drop_path > 0. else nn.Identity()
        self.norm2 = nn.LayerNorm(dim)
        mlp_hidden_dim = int(dim * mlp_ratio)
        self.mlp = Mlp(in_features=dim, hidden_features=mlp_hidden_dim, drop=drop)

    def forward(self, x):
        B, C, H, W = x.shape
        x = x.flatten(2).transpose(1, 2)
        x = x + self.drop_path(self.attn(self.norm1(x)))
        x = x + self.drop_path(self.mlp(self.norm2(x)))
        x = x.transpose(1, 2).view(B, C, H, W)
        return x


class UpBlock(nn.Module):
    def __init__(self, in_channels1, in_channels2, out_channels, bilinear=True):
        super().__init__()
        self.bilinear = bilinear
        if bilinear:
            self.conv1x1 = nn.Conv2d(in_channels1, in_channels2, kernel_size=1)
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False)
        else:
            self.up = nn.ConvTranspose2d(in_channels1, in_channels2, kernel_size=2, stride=2)
        self.conv1 = ConvBlock(in_channels2 * 2, out_channels, kernel_size=1)
        self.trans = TransformerBlock(dim=out_channels, num_heads=out_channels//48)
        self.conv2 = ConvBlock(out_channels, out_channels)

    def forward(self, x1, x2):
        if self.bilinear:
            x1 = self.conv1x1(x1)
        x1 = self.up(x1)
        x = torch.cat([x2, x1], dim=1)
        x = self.conv1(x)
        x = self.trans(x)
        return self.conv2(x)


class Decoder(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.num_classes = num_classes
        self.conv1 = ConvBlock(768 + 96, 96)
        self.conv2 = ConvBlock(768 + 192, 192)
        self.conv3 = ConvBlock(768 + 384, 384)
        self.conv4 = ConvBlock(768 + 768, 768)

        self.trans1 = TransformerBlock(dim=96, num_heads=2)
        self.trans2 = TransformerBlock(dim=192, num_heads=4)
        self.trans3 = TransformerBlock(dim=384, num_heads=8)
        self.trans4 = TransformerBlock(dim=768, num_heads=16)

        self.up1 = UpBlock(768, 384, 384)
        self.up2 = UpBlock(384, 192, 192)
        self.up3 = UpBlock(192, 96, 96)
        self.up4 = ConvBlock(96, 96)

        self.final = nn.Conv2d(96, self.num_classes, kernel_size=3, padding=1)
        self.out = nn.Upsample(scale_factor=4, mode='bilinear', align_corners=False)

    def forward(self, features1, features2=None):
        x1, x2, x3, x4 = features1
        s1, s2, s3, s4, edge1, edge2, edge3, edge4 = features2

        x1 = torch.cat([x1, s1], dim=1)
        x2 = torch.cat([x2, s2], dim=1)
        x3 = torch.cat([x3, s3], dim=1)
        x4 = torch.cat([x4, s4], dim=1)

        x1 = self.conv1(x1)
        x2 = self.conv2(x2)
        x3 = self.conv3(x3)
        x4 = self.conv4(x4)

        x1 = self.trans1(x1)
        x2 = self.trans2(x2)
        x3 = self.trans3(x3)
        x4 = self.trans4(x4)

        f1 = self.up1(x4, x3)
        f2 = self.up2(f1, x2)
        f3 = self.up3(f2, x1)
        f4 = self.up4(f3)

        final = self.final(f4)
        out = self.out(final)

        return out, edge1, edge2, edge3, edge4


class Dino_vit(nn.Module):
    def __init__(self):
        super().__init__()
        self.backbone = torch.hub.load(
                        repo_or_dir=r"Charon\dinov3",
                        model="dinov3_vitb16",
                        source="local",
                        weights=r"Charon\pretrain\dinov3_vitb16_pretrain.pth",
                        pretrained=True,
                    )

        self.adapter = DINOv3_Adapter(
            self.backbone,
            interaction_indexes=[2, 5, 8, 11],
            deform_num_heads=12,
            deform_ratio=1,
            n_points=4,
        )

    def forward(self, x):
        if x.size()[1] == 1:
            x = x.repeat(1, 3, 1, 1)

        return self.adapter(x)


class SimpleConvEncoder(nn.Module):
    def __init__(self):
        super().__init__()

        out_channels = [96, 192, 384, 768]

        self.stage1 = nn.Sequential(
            DoubleConv(3, 48),
            ConvDown(48, 48),
            DoubleConv(48, out_channels[0]),
            ConvDown(out_channels[0], out_channels[0]),
        )

        self.stage2 = nn.Sequential(
            DoubleConv(out_channels[0], out_channels[1]),
            ConvDown(out_channels[1], out_channels[1]),
        )

        self.stage3 = nn.Sequential(
            DoubleConv(out_channels[1], out_channels[2]),
            ConvDown(out_channels[2], out_channels[2]),
        )

        self.stage4 = nn.Sequential(
            DoubleConv(out_channels[2], out_channels[3]),
            ConvDown(out_channels[3], out_channels[3]),
        )

        self.edge_head1 = nn.Sequential(
            DoubleConv(out_channels[0], 48),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
            DoubleConv(48, 24),
            nn.Conv2d(24, 1, kernel_size=3, padding=1),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
        )

        self.edge_head2 = nn.Sequential(
            DoubleConv(out_channels[1], out_channels[0]),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
        )

        self.edge_head3 = nn.Sequential(
            DoubleConv(out_channels[2], out_channels[1]),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
        )

        self.edge_head4 = nn.Sequential(
            DoubleConv(out_channels[3], out_channels[2]),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
        )

    def forward(self, x):
        if x.size()[1] == 1:
            x = x.repeat(1, 3, 1, 1)

        f1 = self.stage1(x)
        f2 = self.stage2(f1)
        f3 = self.stage3(f2)
        f4 = self.stage4(f3)

        edge1 = self.edge_head1(f1)
        edge2 = self.edge_head1(self.edge_head2(f2))
        edge3 = self.edge_head1(self.edge_head2(self.edge_head3(f3)))
        edge4 = self.edge_head1(self.edge_head2(self.edge_head3(self.edge_head4(f4))))

        return f1, f2, f3, f4, edge1, edge2, edge3, edge4


class Dino_seg(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.dino_vit = Dino_vit()
        self.dino_conv = SimpleConvEncoder()
        self.decoder = Decoder(num_classes)

    def forward(self, x):
        return self.decoder(self.dino_vit(x), self.dino_conv(x))


if __name__ == "__main__":
    model = Dino_seg(num_classes=9)
    print(model)
    x = torch.randn(1, 3, 224, 224)
    y, _, _, _, _ = model(x)
    print(y.shape)
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    dino_params = sum(p.numel() for p in model.dino_vit.backbone.parameters())
    adapter_params = sum(p.numel() for p in model.dino_vit.adapter.parameters()) - dino_params
    cnn_params = sum(p.numel() for p in model.dino_conv.parameters())
    decoder_params = sum(p.numel() for p in model.decoder.parameters())
    print("-" * 50)
    print(f"总参数: {total_params:,}")
    print(f"可训练参数量: {trainable_params:,}")
    print(f"dino参数量: {dino_params:,}")
    print(f"adapter参数量: {adapter_params:,}")
    print(f"cnn参数量: {cnn_params:,}")
    print(f"decoder参数量: {decoder_params:,}")
