The tables below show maximum classification time (in microseconds) for sklearn-porter's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex |  824  |    268    |
| Asfault-roads     |  4896 |     -     |
| Asfault-streets   |  6080 |     -     |
| GasSensorArray    | 15312 |     -     |
| PenDigits         |  1560 |     -     |
| HAR               |   -   |     -     |


#### MK20DX256VLH7
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex |  164  |     71    |
| Asfault-roads     |  943  |     52    |
| Asfault-streets   |  1180 |     52    |
| GasSensorArray    |  2775 |     73    |
| PenDigits         |  298  |     -     |
| HAR               | 12055 |     59    |


#### MK66FX1M0VMD18
|                   |  SVM | Dec. Tree |
|-------------------|:----:|:---------:|
| Aedes aegypti-sex |  44  |     23    |
| Asfault-roads     |  267 |     18    |
| Asfault-streets   |  334 |     19    |
| GasSensorArray    |  783 |     28    |
| PenDigits         |  89  |     20    |
| HAR               | 3371 |     21    |
