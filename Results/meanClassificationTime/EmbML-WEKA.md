The tables below show mean classification time (in microseconds) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |    SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:--------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  3107.74 |   46.49   | 26299.12 |  1572.47  |
| Asfault-roads     | 10669.23 |   47.58   |     -    |  4998.81  |
| Asfault-streets   | 15595.86 |   53.37   |     -    |  8143.17  |
| GasSensorArray    |     -    |   71.44   |     -    |  16064.69 |
| PenDigits         |  7484.68 |     -     |  8166.85 |  19559.18 |
| HAR               |     -    |     -     |     -    |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |    SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:--------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  2829.39 |   29.33   | 26320.83 |  1442.23  |
| Asfault-roads     | 11105.23 |   29.96   |     -    |  5570.49  |
| Asfault-streets   | 16299.16 |   33.14   |     -    |  7727.00  |
| GasSensorArray    |     -    |   43.81   |     -    |  18016.90 |
| PenDigits         |  7657.73 |     -     |  5006.70 |  10429.89 |
| HAR               |     -    |     -     |     -    |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |    SVM   | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:--------:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex |  1980.78 |   22.39   | 9961.82 |   556.95  |
| Asfault-roads     |  5009.61 |   22.05   |    -    |  2271.97  |
| Asfault-streets   |  6399.72 |   23.74   |    -    |  2921.01  |
| GasSensorArray    | 15748.91 |   31.35   |    -    |  7070.42  |
| PenDigits         |  3031.12 |   34.19   | 2641.67 |  3431.81  |
| HAR               |     -    |   31.08   |    -    |     -     |


#### MK20DX256VLH7  (floating-point representation)
|                   |    SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:--------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  327.04  |    8.59   |  4055.62 |   248.59  |
| Asfault-roads     |  1099.89 |    8.94   |  8119.16 |   818.15  |
| Asfault-streets   |  1564.64 |    9.78   |  8226.10 |  1410.42  |
| GasSensorArray    |  4781.16 |   13.32   | 24476.09 |  3060.08  |
| PenDigits         |  819.79  |   13.30   |  1686.63 |  5321.92  |
| HAR               | 19781.84 |   11.69   |     -    |  7655.55  |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |   SVM   | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:-------:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex |  115.35 |    3.40   |  608.71 |   52.31   |
| Asfault-roads     |  266.95 |    3.26   | 1262.75 |   184.15  |
| Asfault-streets   |  337.04 |    3.60   | 1277.72 |   253.68  |
| GasSensorArray    |  841.58 |    4.57   | 4147.68 |   516.12  |
| PenDigits         |  148.28 |    4.66   |  173.18 |   365.68  |
| HAR               | 3586.35 |    4.42   |    -    |  2011.93  |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |   SVM   | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:-------:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex |  30.81  |    3.41   |  412.35 |   40.93   |
| Asfault-roads     |  137.80 |    3.11   |  945.71 |   158.14  |
| Asfault-streets   |  209.86 |    3.32   |  957.64 |   205.08  |
| GasSensorArray    |  588.12 |    4.33   | 3365.18 |   457.31  |
| PenDigits         |  136.40 |    4.63   |  120.08 |   270.20  |
| HAR               | 2530.69 |    4.21   |    -    |  1820.07  |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |   SVM  | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  11.13 |    1.61   |  567.08  |   51.58   |
| Asfault-roads     |  34.54 |    1.47   |  978.61  |   141.38  |
| Asfault-streets   |  50.06 |    1.66   |  996.84  |   278.83  |
| GasSensorArray    | 138.88 |    2.07   |  1898.66 |   555.13  |
| PenDigits         |  32.57 |    1.96   |  388.28  |  1475.92  |
| HAR               | 611.38 |    1.84   | 20241.69 |   790.10  |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |   SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:-------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  36.01  |    1.24   |  222.00  |   19.42   |
| Asfault-roads     |  89.54  |    1.05   |  483.35  |   68.54   |
| Asfault-streets   |  118.50 |    1.22   |  489.47  |   93.71   |
| GasSensorArray    |  304.01 |    1.70   |  1656.64 |   198.53  |
| PenDigits         |  56.28  |    1.58   |   55.33  |   123.14  |
| HAR               | 1313.99 |    1.54   | 25316.01 |   791.95  |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |   SVM   | Dec. Tree |    MLP   | Log. Reg. |
|-------------------|:-------:|:---------:|:--------:|:---------:|
| Aedes aegypti-sex |  12.07  |    1.16   |  157.42  |   15.59   |
| Asfault-roads     |  54.90  |    1.13   |  367.84  |   61.91   |
| Asfault-streets   |  83.48  |    1.23   |  373.08  |   80.48   |
| GasSensorArray    |  231.54 |    1.53   |  1350.66 |   179.87  |
| PenDigits         |  53.41  |    1.48   |   40.97  |   94.86   |
| HAR               | 1015.08 |    1.39   | 24067.42 |   726.66  |
