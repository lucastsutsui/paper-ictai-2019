The tables below show flash memory consumption (in bytes) for sklearn-porter's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex | 14946 |   19172   |
| Asfault-roads     | 15968 |     -     |
| Asfault-streets   | 16230 |     -     |
| GasSensorArray    | 18020 |     -     |
| PenDigits         | 15144 |     -     |
| HAR               |   -   |     -     |


#### MK20DX256VLH7
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex | 34248 |   43056   |
| Asfault-roads     | 35984 |   47176   |
| Asfault-streets   | 36512 |   49696   |
| GasSensorArray    | 40160 |   56536   |
| PenDigits         | 34624 |     -     |
| HAR               | 60944 |   53808   |


#### MK66FX1M0VMD18
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex | 37068 |   45876   |
| Asfault-roads     | 38868 |   49932   |
| Asfault-streets   | 39388 |   52508   |
| GasSensorArray    | 42972 |   59348   |
| PenDigits         | 37500 |   155876  |
| HAR               | 63756 |   56620   |
