The tables below show maximum classification time (in microseconds) for m2cgen's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |  SVM  | Dec. Tree | Log. Reg. |
|-------------------|:-----:|:---------:|:---------:|
| Aedes aegypti-sex |  788  |    120    |    780    |
| Asfault-roads     |  4712 |    112    |    4756   |
| Asfault-streets   |  5868 |    120    |    5908   |
| GasSensorArray    | 14336 |    160    |   14476   |
| PenDigits         |  1424 |    192    |    1424   |
| HAR               | 61312 |    136    |   61556   |


#### MK20DX256VLH7
|                   |  SVM | Dec. Tree | Log. Reg. |
|-------------------|:----:|:---------:|:---------:|
| Aedes aegypti-sex |  94  |     33    |     94    |
| Asfault-roads     |  492 |     25    |    511    |
| Asfault-streets   |  639 |     26    |    639    |
| GasSensorArray    | 1428 |     35    |    1427   |
| PenDigits         |  167 |     34    |    165    |
| HAR               | 6656 |     30    |    6648   |


#### MK66FX1M0VMD18
|                   | SVM | Dec. Tree | Log. Reg. |
|-------------------|:---:|:---------:|:---------:|
| Aedes aegypti-sex |  4  |     4     |     4     |
| Asfault-roads     |  16 |     4     |     17    |
| Asfault-streets   |  20 |     4     |     20    |
| GasSensorArray    |  64 |     5     |     65    |
| PenDigits         |  6  |     7     |     6     |
| HAR               | 311 |     5     |    311    |
