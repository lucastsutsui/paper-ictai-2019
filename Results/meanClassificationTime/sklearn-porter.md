The tables below show mean classification time (in microseconds) for sklearn-porter's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |    SVM   | Dec. Tree |
|-------------------|:--------:|:---------:|
| Aedes aegypti-sex |  792.77  |   153.42  |
| Asfault-roads     |  4813.40 |     -     |
| Asfault-streets   |  5953.19 |     -     |
| GasSensorArray    | 15129.27 |     -     |
| PenDigits         |  1520.61 |     -     |
| HAR               |     -    |     -     |


#### MK20DX256VLH7
|                   |    SVM   | Dec. Tree |
|-------------------|:--------:|:---------:|
| Aedes aegypti-sex |  151.91  |   36.62   |
| Asfault-roads     |  927.47  |   28.64   |
| Asfault-streets   |  1165.81 |   33.20   |
| GasSensorArray    |  2763.61 |   31.73   |
| PenDigits         |  290.85  |     -     |
| HAR               | 11991.95 |   37.08   |


#### MK66FX1M0VMD18
|                   |   SVM   | Dec. Tree |
|-------------------|:-------:|:---------:|
| Aedes aegypti-sex |  42.03  |   13.24   |
| Asfault-roads     |  262.24 |   10.45   |
| Asfault-streets   |  329.48 |   12.07   |
| GasSensorArray    |  777.69 |   11.24   |
| PenDigits         |  86.80  |   11.91   |
| HAR               | 3344.85 |   12.90   |
