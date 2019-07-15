The tables below show SRAM memory consumption (in bytes) for sklearn-porter's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |  SVM | Dec. Tree |
|-------------------|:----:|:---------:|
| Aedes aegypti-sex | 1398 |    5808   |
| Asfault-roads     | 2360 |     -     |
| Asfault-streets   | 2622 |     -     |
| GasSensorArray    | 4668 |     -     |
| PenDigits         | 1452 |     -     |
| HAR               |   -  |     -     |


#### MK20DX256VLH7
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex |  4688 |   13496   |
| Asfault-roads     |  6512 |   17640   |
| Asfault-streets   |  7032 |   20152   |
| GasSensorArray    | 10880 |   27256   |
| PenDigits         |  4928 |     -     |
| HAR               | 33396 |   26260   |


#### MK66FX1M0VMD18
|                   |  SVM  | Dec. Tree |
|-------------------|:-----:|:---------:|
| Aedes aegypti-sex |  5072 |   13880   |
| Asfault-roads     |  6896 |   18024   |
| Asfault-streets   |  7416 |   20536   |
| GasSensorArray    | 11264 |   27640   |
| PenDigits         |  5312 |   123688  |
| HAR               | 33780 |   26644   |
