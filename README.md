# Glasses: Adapter-Enhanced DINOv3 with Boundary-Aware Multi-Scale Representations for Medical Image Segmentation


## Results on Synapse Dataset

| Method | Dice↑ | HD↓ | Aorta | Gallbladder | Kidney(L) | Kidney(R) | Liver | Pancreas | Spleen | Stomach |
|--------|-------|-----|-------|-------------|-----------|-----------|-------|----------|--------|---------|
| U-Net | 76.85 | 39.70 | 89.07 | 69.72 | 77.77 | 68.60 | 93.43 | 53.98 | 86.67 | 75.58 |
| nnUNet | 79.40 | 14.57 | 90.24 | 44.23 | 87.30 | 87.94 | 90.10 | 70.10 | 85.45 | 79.82 |
| TransUNet | 77.48 | 31.69 | 87.23 | 63.13 | 81.87 | 77.02 | 94.08 | 55.86 | 85.08 | 75.62 |
| Swin-Unet | 79.13 | 21.55 | 85.47 | 66.53 | 83.28 | 79.61 | 94.29 | 56.58 | 90.66 | 76.60 |
| Mamba-Unet | 80.58 | 21.95 | 87.23 | 68.25 | 84.66 | 80.41 | 94.03 | 58.92 | 90.12 | 81.05 |
| HiFormer | 80.39 | 14.70 | 86.21 | 65.69 | 85.23 | 79.77 | 94.61 | 59.52 | 90.99 | 81.08 |
| MISSFormer | 81.96 | 18.20 | 86.99 | 68.65 | 85.21 | 82.00 | 94.41 | 65.67 | 91.92 | 80.81 |
| Effformer | 80.79 | 17.00 | 85.81 | 66.89 | 84.10 | 81.81 | 94.80 | 62.25 | 91.05 | 79.58 |
| DAE-Former | 82.63 | 16.39 | 87.84 | 71.65 | 87.66 | 82.39 | 95.08 | 63.93 | 91.82 | 80.77 |
| GLoG-GSUnet | 83.36 | 23.02 | 88.43 | 73.20 | 84.50 | 80.98 | 95.14 | 71.02 | 91.51 | 82.10 |
| CASTformer | 82.55 | 22.73 | 89.05 | 67.48 | 86.05 | 82.17 | 95.61 | 67.49 | 91.00 | 81.55 |
| PVT-CASCADE | 81.06 | 20.23 | 83.01 | 70.59 | 82.23 | 80.37 | 94.08 | 64.43 | 90.10 | 83.69 |
| Rskd | 82.33 | 17.21 | 87.11 | 68.56 | 86.68 | 84.54 | 93.51 | 65.40 | 90.06 | 82.81 |
| **Ours** | **83.52** | **12.28** | 88.34 | 70.59 | 88.38 | 86.24 | 95.12 | 63.25 | 91.66 | 84.60 |

<div style="overflow-x:auto;">

<table>
<tr>
<th>Method</th>
<th>Dice↑</th>
<th>HD↓</th>
<th>Aorta</th>
<th>Gallbladder</th>
<th>Kidney(L)</th>
<th>Kidney(R)</th>
<th>Liver</th>
<th>Pancreas</th>
<th>Spleen</th>
<th>Stomach</th>
</tr>

<tr>
<td nowrap>U-Net</td>
<td nowrap>76.85</td>
<td nowrap>39.70</td>
<td nowrap>89.07</td>
<td nowrap>69.72</td>
<td nowrap>77.77</td>
<td nowrap>68.60</td>
<td nowrap>93.43</td>
<td nowrap>53.98</td>
<td nowrap>86.67</td>
<td nowrap>75.58</td>
</tr>

<tr>
<td nowrap>nnUNet</td>
<td nowrap>79.40</td>
<td nowrap>14.57</td>
<td nowrap>90.24</td>
<td nowrap>44.23</td>
<td nowrap>87.30</td>
<td nowrap>87.94</td>
<td nowrap>90.10</td>
<td nowrap>70.10</td>
<td nowrap>85.45</td>
<td nowrap>79.82</td>
</tr>

<tr>
<td nowrap>TransUNet</td>
<td nowrap>77.48</td>
<td nowrap>31.69</td>
<td nowrap>87.23</td>
<td nowrap>63.13</td>
<td nowrap>81.87</td>
<td nowrap>77.02</td>
<td nowrap>94.08</td>
<td nowrap>55.86</td>
<td nowrap>85.08</td>
<td nowrap>75.62</td>
</tr>

<tr>
<td nowrap>Swin-Unet</td>
<td nowrap>79.13</td>
<td nowrap>21.55</td>
<td nowrap>85.47</td>
<td nowrap>66.53</td>
<td nowrap>83.28</td>
<td nowrap>79.61</td>
<td nowrap>94.29</td>
<td nowrap>56.58</td>
<td nowrap>90.66</td>
<td nowrap>76.60</td>
</tr>

<tr>
<td nowrap>Mamba-Unet</td>
<td nowrap>80.58</td>
<td nowrap>21.95</td>
<td nowrap>87.23</td>
<td nowrap>68.25</td>
<td nowrap>84.66</td>
<td nowrap>80.41</td>
<td nowrap>94.03</td>
<td nowrap>58.92</td>
<td nowrap>90.12</td>
<td nowrap>81.05</td>
</tr>

<tr>
<td nowrap>HiFormer</td>
<td nowrap>80.39</td>
<td nowrap>14.70</td>
<td nowrap>86.21</td>
<td nowrap>65.69</td>
<td nowrap>85.23</td>
<td nowrap>79.77</td>
<td nowrap>94.61</td>
<td nowrap>59.52</td>
<td nowrap>90.99</td>
<td nowrap>81.08</td>
</tr>

<tr>
<td nowrap>MISSFormer</td>
<td nowrap>81.96</td>
<td nowrap>18.20</td>
<td nowrap>86.99</td>
<td nowrap>68.65</td>
<td nowrap>85.21</td>
<td nowrap>82.00</td>
<td nowrap>94.41</td>
<td nowrap>65.67</td>
<td nowrap>91.92</td>
<td nowrap>80.81</td>
</tr>

<tr>
<td nowrap>Effformer</td>
<td nowrap>80.79</td>
<td nowrap>17.00</td>
<td nowrap>85.81</td>
<td nowrap>66.89</td>
<td nowrap>84.10</td>
<td nowrap>81.81</td>
<td nowrap>94.80</td>
<td nowrap>62.25</td>
<td nowrap>91.05</td>
<td nowrap>79.58</td>
</tr>

<tr>
<td nowrap>DAE-Former</td>
<td nowrap>82.63</td>
<td nowrap>16.39</td>
<td nowrap>87.84</td>
<td nowrap>71.65</td>
<td nowrap>87.66</td>
<td nowrap>82.39</td>
<td nowrap>95.08</td>
<td nowrap>63.93</td>
<td nowrap>91.82</td>
<td nowrap>80.77</td>
</tr>

<tr>
<td nowrap>GLoG-GSUnet</td>
<td nowrap>83.36</td>
<td nowrap>23.02</td>
<td nowrap>88.43</td>
<td nowrap>73.20</td>
<td nowrap>84.50</td>
<td nowrap>80.98</td>
<td nowrap>95.14</td>
<td nowrap>71.02</td>
<td nowrap>91.51</td>
<td nowrap>82.10</td>
</tr>

<tr>
<td nowrap>CASTformer</td>
<td nowrap>82.55</td>
<td nowrap>22.73</td>
<td nowrap>89.05</td>
<td nowrap>67.48</td>
<td nowrap>86.05</td>
<td nowrap>82.17</td>
<td nowrap>95.61</td>
<td nowrap>67.49</td>
<td nowrap>91.00</td>
<td nowrap>81.55</td>
</tr>

<tr>
<td nowrap>PVT-CASCADE</td>
<td nowrap>81.06</td>
<td nowrap>20.23</td>
<td nowrap>83.01</td>
<td nowrap>70.59</td>
<td nowrap>82.23</td>
<td nowrap>80.37</td>
<td nowrap>94.08</td>
<td nowrap>64.43</td>
<td nowrap>90.10</td>
<td nowrap>83.69</td>
</tr>

<tr>
<td nowrap>Rskd</td>
<td nowrap>82.33</td>
<td nowrap>17.21</td>
<td nowrap>87.11</td>
<td nowrap>68.56</td>
<td nowrap>86.68</td>
<td nowrap>84.54</td>
<td nowrap>93.51</td>
<td nowrap>65.40</td>
<td nowrap>90.06</td>
<td nowrap>82.81</td>
</tr>

<tr>
<td nowrap><b>Ours</b></td>
<td nowrap><b>83.52</b></td>
<td nowrap><b>12.28</b></td>
<td nowrap>88.34</td>
<td nowrap>70.59</td>
<td nowrap>88.38</td>
<td nowrap>86.24</td>
<td nowrap>95.12</td>
<td nowrap>63.25</td>
<td nowrap>91.66</td>
<td nowrap>84.60</td>
</tr>

</table>

</div>
