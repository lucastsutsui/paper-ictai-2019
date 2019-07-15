The tables below show flash memory consumption (in bytes) for emlearn's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   | Dec. Tree | MLP |
|-------------------|:---------:|:---:|
| Aedes aegypti-sex |   18044   |  -  |
| Asfault-roads     |   16324   |  -  |
| Asfault-streets   |   18974   |  -  |
| GasSensorArray    |   25456   |  -  |
| PenDigits         |   52726   |  -  |
| HAR               |   23750   |  -  |


#### MK20DX256VLH7
|                   | Dec. Tree |  MLP  |
|-------------------|:---------:|:-----:|
| Aedes aegypti-sex |   35872   | 56440 |
| Asfault-roads     |   35168   | 66448 |
| Asfault-streets   |   35744   | 66856 |
| GasSensorArray    |   39136   | 92856 |
| PenDigits         |   53856   | 46472 |
| HAR               |   37920   |   -   |


#### MK66FX1M0VMD18
|                   | Dec. Tree |   MLP  |
|-------------------|:---------:|:------:|
| Aedes aegypti-sex |   38556   |  57460 |
| Asfault-roads     |   37788   |  67468 |
| Asfault-streets   |   38436   |  67876 |
| GasSensorArray    |   42140   |  93876 |
| PenDigits         |   56924   |  47492 |
| HAR               |   41180   | 267076 |
