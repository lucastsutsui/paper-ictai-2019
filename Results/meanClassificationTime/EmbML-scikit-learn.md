The tables below show mean classification time (in microseconds) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |    SVM   | Dec. Tree | MLP | Log. Reg. |
|-------------------|:--------:|:---------:|:---:|:---------:|
| Aedes aegypti-sex |  1379.43 |   107.30  |  -  |  1382.83  |
| Asfault-roads     |  4906.53 |   83.18   |  -  |  4918.08  |
| Asfault-streets   |  6086.57 |   96.48   |  -  |  6111.57  |
| GasSensorArray    | 14958.52 |   88.71   |  -  |  15106.58 |
| PenDigits         |  1504.24 |     -     |  -  |  1508.19  |
| HAR               |     -    |     -     |  -  |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |    SVM   | Dec. Tree | MLP | Log. Reg. |
|-------------------|:--------:|:---------:|:---:|:---------:|
| Aedes aegypti-sex |  868.96  |   66.95   |  -  |   885.33  |
| Asfault-roads     |  5131.72 |   52.54   |  -  |  5147.36  |
| Asfault-streets   |  6428.47 |   62.07   |  -  |  6410.91  |
| GasSensorArray    | 13519.15 |   56.04   |  -  |  10509.98 |
| PenDigits         |  1471.69 |     -     |  -  |  1485.17  |
| HAR               |     -    |     -     |  -  |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |   SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:-------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  193.59 |   41.67   |     -    |   306.15  |
| Asfault-roads     | 1578.91 |   38.07   |     -    |  1576.63  |
| Asfault-streets   | 1900.61 |   36.72   |     -    |  1920.05  |
| GasSensorArray    | 1495.83 |   33.71   |     -    |  1550.10  |
| PenDigits         |  197.09 |     -     | 16457.69 |   346.67  |
| HAR               |    -    |     -     |     -    |     -     |

#### MK20DX256VLH7  (floating-point representation)
|                   |   SVM   | Dec. Tree |    MLP    | Log. Reg. |
|-------------------|:-------:|:---------:|:---------:|:---------:|
| Aedes aegypti-sex |  144.66 |   19.99   |  10035.30 |   144.79  |
| Asfault-roads     |  514.60 |   14.92   |  15548.66 |   513.38  |
| Asfault-streets   |  649.10 |   17.10   |  15825.15 |   647.23  |
| GasSensorArray    | 1534.63 |   16.44   |  30848.53 |  1530.07  |
| PenDigits         |  170.58 |   17.14   |  4012.01  |   170.05  |
| HAR               | 6943.96 |   18.10   | 131105.71 |  6936.18  |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |   SVM  | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  23.58 |    7.01   |  2211.37 |   23.58   |
| Asfault-roads     |  67.38 |    5.31   |  3463.84 |   67.39   |
| Asfault-streets   |  83.93 |    6.15   |  3514.89 |   83.93   |
| GasSensorArray    | 196.04 |    5.86   |  6805.94 |   192.44  |
| PenDigits         |  24.30 |    6.12   |  972.03  |   24.30   |
| HAR               | 848.43 |    6.49   | 28508.80 |   848.43  |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |   SVM  | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  22.62 |    5.67   |  2080.93 |   23.13   |
| Asfault-roads     |  69.68 |    4.99   |  3251.75 |   69.62   |
| Asfault-streets   |  82.87 |    4.86   |  3309.49 |   83.15   |
| GasSensorArray    | 180.19 |    4.81   |  6267.42 |   180.09  |
| PenDigits         |  22.50 |    5.98   |  915.60  |   23.12   |
| HAR               | 824.25 |    4.90   | 26291.28 |   832.10  |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |   SVM  | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex |  4.54  |    2.74   |  654.26 |    4.54   |
| Asfault-roads     |  17.95 |    2.21   |  983.07 |   17.95   |
| Asfault-streets   |  22.46 |    2.76   |  994.53 |   22.46   |
| GasSensorArray    |  54.04 |    2.48   | 1925.95 |   54.04   |
| PenDigits         |  6.77  |    2.73   |  259.21 |    6.77   |
| HAR               | 169.87 |    2.66   | 9149.05 |   169.88  |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |   SVM  | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  8.78  |    2.52   |  852.23  |    8.82   |
| Asfault-roads     |  25.61 |    1.90   |  1331.26 |   25.63   |
| Asfault-streets   |  31.75 |    2.30   |  1349.90 |   31.75   |
| GasSensorArray    |  73.81 |    2.13   |  2621.73 |   71.88   |
| PenDigits         |  9.02  |    2.41   |  359.29  |    9.03   |
| HAR               | 343.15 |    2.50   | 11892.27 |   343.09  |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |   SVM  | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  8.70  |    2.10   |  794.89  |    8.87   |
| Asfault-roads     |  26.85 |    1.91   |  1275.43 |   26.84   |
| Asfault-streets   |  31.94 |    1.88   |  1294.96 |   31.97   |
| GasSensorArray    |  70.19 |    1.93   |  2550.54 |   70.23   |
| PenDigits         |  8.72  |    2.41   |  342.55  |    8.95   |
| HAR               | 324.37 |    1.96   | 11296.79 |   326.14  |
