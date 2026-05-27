# Glasses: Adapter-Enhanced DINOv3 with Boundary-Aware Multi-Scale Representations for Medical Image Segmentation


## Results on Synapse Dataset


<div align="center" style="overflow-x:auto;">

<table>
<tr>
<th align="center">Method</th>
<th align="center">Dice↑</th>
<th align="center">HD↓</th>
<th align="center">Aorta</th>
<th align="center">Gallbladder</th>
<th align="center">Kidney(L)</th>
<th align="center">Kidney(R)</th>
<th align="center">Liver</th>
<th align="center">Pancreas</th>
<th align="center">Spleen</th>
<th align="center">Stomach</th>
</tr>

<tr>
<td align="center" nowrap>U-Net</td>
<td align="center" nowrap>76.85</td>
<td align="center" nowrap>39.70</td>
<td align="center" nowrap>89.07</td>
<td align="center" nowrap>69.72</td>
<td align="center" nowrap>77.77</td>
<td align="center" nowrap>68.60</td>
<td align="center" nowrap>93.43</td>
<td align="center" nowrap>53.98</td>
<td align="center" nowrap>86.67</td>
<td align="center" nowrap>75.58</td>
</tr>

<tr>
<td align="center" nowrap>nnUNet</td>
<td align="center" nowrap>79.40</td>
<td align="center" nowrap>14.57</td>
<td align="center" nowrap>90.24</td>
<td align="center" nowrap>44.23</td>
<td align="center" nowrap>87.30</td>
<td align="center" nowrap>87.94</td>
<td align="center" nowrap>90.10</td>
<td align="center" nowrap>70.10</td>
<td align="center" nowrap>85.45</td>
<td align="center" nowrap>79.82</td>
</tr>

<tr>
<td align="center" nowrap>TransUNet</td>
<td align="center" nowrap>77.48</td>
<td align="center" nowrap>31.69</td>
<td align="center" nowrap>87.23</td>
<td align="center" nowrap>63.13</td>
<td align="center" nowrap>81.87</td>
<td align="center" nowrap>77.02</td>
<td align="center" nowrap>94.08</td>
<td align="center" nowrap>55.86</td>
<td align="center" nowrap>85.08</td>
<td align="center" nowrap>75.62</td>
</tr>

<tr>
<td align="center" nowrap>Swin-Unet</td>
<td align="center" nowrap>79.13</td>
<td align="center" nowrap>21.55</td>
<td align="center" nowrap>85.47</td>
<td align="center" nowrap>66.53</td>
<td align="center" nowrap>83.28</td>
<td align="center" nowrap>79.61</td>
<td align="center" nowrap>94.29</td>
<td align="center" nowrap>56.58</td>
<td align="center" nowrap>90.66</td>
<td align="center" nowrap>76.60</td>
</tr>

<tr>
<td align="center" nowrap>Mamba-Unet</td>
<td align="center" nowrap>80.58</td>
<td align="center" nowrap>21.95</td>
<td align="center" nowrap>87.23</td>
<td align="center" nowrap>68.25</td>
<td align="center" nowrap>84.66</td>
<td align="center" nowrap>80.41</td>
<td align="center" nowrap>94.03</td>
<td align="center" nowrap>58.92</td>
<td align="center" nowrap>90.12</td>
<td align="center" nowrap>81.05</td>
</tr>

<tr>
<td align="center" nowrap>HiFormer</td>
<td align="center" nowrap>80.39</td>
<td align="center" nowrap>14.70</td>
<td align="center" nowrap>86.21</td>
<td align="center" nowrap>65.69</td>
<td align="center" nowrap>85.23</td>
<td align="center" nowrap>79.77</td>
<td align="center" nowrap>94.61</td>
<td align="center" nowrap>59.52</td>
<td align="center" nowrap>90.99</td>
<td align="center" nowrap>81.08</td>
</tr>

<tr>
<td align="center" nowrap>MISSFormer</td>
<td align="center" nowrap>81.96</td>
<td align="center" nowrap>18.20</td>
<td align="center" nowrap>86.99</td>
<td align="center" nowrap>68.65</td>
<td align="center" nowrap>85.21</td>
<td align="center" nowrap>82.00</td>
<td align="center" nowrap>94.41</td>
<td align="center" nowrap>65.67</td>
<td align="center" nowrap>91.92</td>
<td align="center" nowrap>80.81</td>
</tr>

<tr>
<td align="center" nowrap>Effformer</td>
<td align="center" nowrap>80.79</td>
<td align="center" nowrap>17.00</td>
<td align="center" nowrap>85.81</td>
<td align="center" nowrap>66.89</td>
<td align="center" nowrap>84.10</td>
<td align="center" nowrap>81.81</td>
<td align="center" nowrap>94.80</td>
<td align="center" nowrap>62.25</td>
<td align="center" nowrap>91.05</td>
<td align="center" nowrap>79.58</td>
</tr>

<tr>
<td align="center" nowrap>DAE-Former</td>
<td align="center" nowrap>82.63</td>
<td align="center" nowrap>16.39</td>
<td align="center" nowrap>87.84</td>
<td align="center" nowrap>71.65</td>
<td align="center" nowrap>87.66</td>
<td align="center" nowrap>82.39</td>
<td align="center" nowrap>95.08</td>
<td align="center" nowrap>63.93</td>
<td align="center" nowrap>91.82</td>
<td align="center" nowrap>80.77</td>
</tr>

<tr>
<td align="center" nowrap>GLoG-GSUnet</td>
<td align="center" nowrap>83.36</td>
<td align="center" nowrap>23.02</td>
<td align="center" nowrap>88.43</td>
<td align="center" nowrap>73.20</td>
<td align="center" nowrap>84.50</td>
<td align="center" nowrap>80.98</td>
<td align="center" nowrap>95.14</td>
<td align="center" nowrap>71.02</td>
<td align="center" nowrap>91.51</td>
<td align="center" nowrap>82.10</td>
</tr>

<tr>
<td align="center" nowrap>CASTformer</td>
<td align="center" nowrap>82.55</td>
<td align="center" nowrap>22.73</td>
<td align="center" nowrap>89.05</td>
<td align="center" nowrap>67.48</td>
<td align="center" nowrap>86.05</td>
<td align="center" nowrap>82.17</td>
<td align="center" nowrap>95.61</td>
<td align="center" nowrap>67.49</td>
<td align="center" nowrap>91.00</td>
<td align="center" nowrap>81.55</td>
</tr>

<tr>
<td align="center" nowrap>PVT-CASCADE</td>
<td align="center" nowrap>81.06</td>
<td align="center" nowrap>20.23</td>
<td align="center" nowrap>83.01</td>
<td align="center" nowrap>70.59</td>
<td align="center" nowrap>82.23</td>
<td align="center" nowrap>80.37</td>
<td align="center" nowrap>94.08</td>
<td align="center" nowrap>64.43</td>
<td align="center" nowrap>90.10</td>
<td align="center" nowrap>83.69</td>
</tr>

<tr>
<td align="center" nowrap>Rskd</td>
<td align="center" nowrap>82.33</td>
<td align="center" nowrap>17.21</td>
<td align="center" nowrap>87.11</td>
<td align="center" nowrap>68.56</td>
<td align="center" nowrap>86.68</td>
<td align="center" nowrap>84.54</td>
<td align="center" nowrap>93.51</td>
<td align="center" nowrap>65.40</td>
<td align="center" nowrap>90.06</td>
<td align="center" nowrap>82.81</td>
</tr>

<tr>
<td align="center" nowrap><b>Ours</b></td>
<td align="center" nowrap><b>83.52</b></td>
<td align="center" nowrap><b>12.28</b></td>
<td align="center" nowrap>88.34</td>
<td align="center" nowrap>70.59</td>
<td align="center" nowrap>88.38</td>
<td align="center" nowrap>86.24</td>
<td align="center" nowrap>95.12</td>
<td align="center" nowrap>63.25</td>
<td align="center" nowrap>91.66</td>
<td align="center" nowrap>84.60</td>
</tr>

</table>

</div>
