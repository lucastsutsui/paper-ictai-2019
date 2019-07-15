The tables below show mean classification time (in microseconds) for m2cgen's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |    SVM   | Dec. Tree | Log. Reg. |
|-------------------|:--------:|:---------:|:---------:|
| Aedes aegypti-sex |  755.16  |   70.07   |   758.45  |
| Asfault-roads     |  4647.27 |   72.32   |  4658.13  |
| Asfault-streets   |  5750.71 |   86.29   |  5775.24  |
| GasSensorArray    | 14159.02 |   88.29   |  14306.93 |
| PenDigits         |  1375.07 |   145.64  |  1378.42  |
| HAR               | 60566.52 |   93.27   |  60806.55 |


#### MK20DX256VLH7
|                   |   SVM   | Dec. Tree | Log. Reg. |
|-------------------|:-------:|:---------:|:---------:|
| Aedes aegypti-sex |  84.68  |   15.70   |   84.75   |
| Asfault-roads     |  480.67 |   14.70   |   502.57  |
| Asfault-streets   |  631.03 |   17.51   |   628.97  |
| GasSensorArray    | 1417.36 |   18.08   |  1414.51  |
| PenDigits         |  160.01 |   24.03   |   159.50  |
| HAR               | 6623.55 |   19.42   |  6614.93  |

#### MK66FX1M0VMD18
|                   |   SVM  | Dec. Tree | Log. Reg. |
|-------------------|:------:|:---------:|:---------:|
| Aedes aegypti-sex |  2.65  |    1.87   |    2.65   |
| Asfault-roads     |  13.40 |    1.55   |   13.67   |
| Asfault-streets   |  16.68 |    2.05   |   16.66   |
| GasSensorArray    |  58.73 |    2.04   |   58.73   |
| PenDigits         |  4.05  |    3.02   |    4.05   |
| HAR               | 309.35 |    2.54   |   309.36  |
