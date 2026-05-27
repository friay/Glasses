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

<table align="center">
<tr>
<th>Method</th>
<th>D↑</th>
<th>HD↓</th>
<th>Aor</th>
<th>Gall</th>
<th>Kid(L)</th>
<th>Kid(R)</th>
<th>Liv</th>
<th>Pan</th>
<th>Spl</th>
<th>Sto</th>
</tr>

<tr><td>U-Net</td><td>76.85</td><td>39.70</td><td>89.07</td><td>69.72</td><td>77.77</td><td>68.60</td><td>93.43</td><td>53.98</td><td>86.67</td><td>75.58</td></tr>

<tr><td>nnUNet</td><td>79.40</td><td>14.57</td><td>90.24</td><td>44.23</td><td>87.30</td><td>87.94</td><td>90.10</td><td>70.10</td><td>85.45</td><td>79.82</td></tr>

<tr><td>TransUNet</td><td>77.48</td><td>31.69</td><td>87.23</td><td>63.13</td><td>81.87</td><td>77.02</td><td>94.08</td><td>55.86</td><td>85.08</td><td>75.62</td></tr>

<tr><td>Swin-Unet</td><td>79.13</td><td>21.55</td><td>85.47</td><td>66.53</td><td>83.28</td><td>79.61</td><td>94.29</td><td>56.58</td><td>90.66</td><td>76.60</td></tr>

<tr><td>Mamba-Unet</td><td>80.58</td><td>21.95</td><td>87.23</td><td>68.25</td><td>84.66</td><td>80.41</td><td>94.03</td><td>58.92</td><td>90.12</td><td>81.05</td></tr>

<tr><td>HiFormer</td><td>80.39</td><td>14.70</td><td>86.21</td><td>65.69</td><td>85.23</td><td>79.77</td><td>94.61</td><td>59.52</td><td>90.99</td><td>81.08</td></tr>

<tr><td>MISSFormer</td><td>81.96</td><td>18.20</td><td>86.99</td><td>68.65</td><td>85.21</td><td>82.00</td><td>94.41</td><td>65.67</td><td>91.92</td><td>80.81</td></tr>

<tr><td>Effformer</td><td>80.79</td><td>17.00</td><td>85.81</td><td>66.89</td><td>84.10</td><td>81.81</td><td>94.80</td><td>62.25</td><td>91.05</td><td>79.58</td></tr>

<tr><td>DAE-Former</td><td>82.63</td><td>16.39</td><td>87.84</td><td>71.65</td><td>87.66</td><td>82.39</td><td>95.08</td><td>63.93</td><td>91.82</td><td>80.77</td></tr>

<tr><td>GLoG-GSUnet</td><td>83.36</td><td>23.02</td><td>88.43</td><td>73.20</td><td>84.50</td><td>80.98</td><td>95.14</td><td>71.02</td><td>91.51</td><td>82.10</td></tr>

<tr><td>CASTformer</td><td>82.55</td><td>22.73</td><td>89.05</td><td>67.48</td><td>86.05</td><td>82.17</td><td>95.61</td><td>67.49</td><td>91.00</td><td>81.55</td></tr>

<tr><td>PVT-CASCADE</td><td>81.06</td><td>20.23</td><td>83.01</td><td>70.59</td><td>82.23</td><td>80.37</td><td>94.08</td><td>64.43</td><td>90.10</td><td>83.69</td></tr>

<tr><td>Rskd</td><td>82.33</td><td>17.21</td><td>87.11</td><td>68.56</td><td>86.68</td><td>84.54</td><td>93.51</td><td>65.40</td><td>90.06</td><td>82.81</td></tr>

<tr>
<td><b>👓 Ours</b></td>
<td><b>83.52</b></td>
<td><b>12.28</b></td>
<td>88.34</td>
<td>70.59</td>
<td>88.38</td>
<td>86.24</td>
<td>95.12</td>
<td>63.25</td>
<td>91.66</td>
<td>84.60</td>
</tr>
</table>
