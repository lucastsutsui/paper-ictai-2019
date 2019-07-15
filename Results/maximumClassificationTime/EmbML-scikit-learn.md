The tables below show maximum classification time (in microseconds) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree | MLP | Log. Reg. |
|-------------------|:-----:|:---------:|:---:|:---------:|
| Aedes aegypti-sex |  1416 |    188    |  -  |    1408   |
| Asfault-roads     |  4972 |    152    |  -  |    5016   |
| Asfault-streets   |  6204 |    152    |  -  |    6248   |
| GasSensorArray    | 15140 |    212    |  -  |   15276   |
| PenDigits         |  1548 |     -     |  -  |    1556   |
| HAR               |   -   |     -     |  -  |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree | MLP | Log. Reg. |
|-------------------|:-----:|:---------:|:---:|:---------:|
| Aedes aegypti-sex |  872  |    120    |  -  |    888    |
| Asfault-roads     |  5148 |     96    |  -  |    5164   |
| Asfault-streets   |  6456 |    100    |  -  |    6436   |
| GasSensorArray    | 13596 |    132    |  -  |   10584   |
| PenDigits         |  1492 |     -     |  -  |    1496   |
| HAR               |   -   |     -     |  -  |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  204 |     68    |   -   |    336    |
| Asfault-roads     | 1720 |     72    |   -   |    1712   |
| Asfault-streets   | 2156 |     72    |   -   |    2184   |
| GasSensorArray    | 1500 |     96    |   -   |    1556   |
| PenDigits         |  204 |     -     | 16840 |    364    |
| HAR               |   -  |     -     |   -   |     -     |

#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex |  154 |     41    |  10065 |    154    |
| Asfault-roads     |  523 |     28    |  15615 |    521    |
| Asfault-streets   |  657 |     28    |  15902 |    657    |
| GasSensorArray    | 1543 |     40    |  30928 |    1540   |
| PenDigits         |  176 |     30    |  4109  |    177    |
| HAR               | 6970 |     31    | 131393 |    6963   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   | SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:---:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  33 |     18    |  2220 |     32    |
| Asfault-roads     |  71 |     12    |  3467 |     71    |
| Asfault-streets   |  88 |     11    |  3517 |     88    |
| GasSensorArray    | 199 |     14    |  6808 |    196    |
| PenDigits         |  27 |     11    |  978  |     27    |
| HAR               | 850 |     12    | 28512 |    850    |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   | SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:---:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  32 |     15    |  2141 |     32    |
| Asfault-roads     |  74 |     10    |  3326 |     73    |
| Asfault-streets   |  87 |     10    |  3383 |     87    |
| GasSensorArray    | 183 |     12    |  6372 |    184    |
| PenDigits         |  25 |     12    |  927  |     26    |
| HAR               | 827 |     11    | 26366 |    834    |


#### MK66FX1M0VMD18  (floating-point representation)
|                   | SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:---:|:---------:|:----:|:---------:|
| Aedes aegypti-sex |  6  |     5     |  660 |     6     |
| Asfault-roads     |  20 |     5     |  988 |     19    |
| Asfault-streets   |  24 |     5     |  999 |     24    |
| GasSensorArray    |  56 |     6     | 1931 |     56    |
| PenDigits         |  8  |     6     |  271 |     8     |
| HAR               | 173 |     6     | 9650 |    173    |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   | SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:---:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  10 |     5     |  857  |     10    |
| Asfault-roads     |  27 |     5     |  1336 |     27    |
| Asfault-streets   |  34 |     5     |  1354 |     34    |
| GasSensorArray    |  77 |     5     |  2627 |     74    |
| PenDigits         |  11 |     6     |  371  |     11    |
| HAR               | 347 |     5     | 12157 |    347    |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   | SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:---:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  10 |     4     |  804  |     10    |
| Asfault-roads     |  28 |     4     |  1288 |     28    |
| Asfault-streets   |  34 |     4     |  1307 |     34    |
| GasSensorArray    |  72 |     5     |  2568 |     72    |
| PenDigits         |  11 |     6     |  347  |     11    |
| HAR               | 327 |     5     | 11327 |    329    |
