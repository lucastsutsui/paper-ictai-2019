The tables below show maximum classification time (in microseconds) for emlearn's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   | Dec. Tree | MLP |
|-------------------|:---------:|:---:|
| Aedes aegypti-sex |     68    |  -  |
| Asfault-roads     |     36    |  -  |
| Asfault-streets   |     36    |  -  |
| GasSensorArray    |    132    |  -  |
| PenDigits         |    108    |  -  |
| HAR               |     56    |  -  |


#### MK20DX256VLH7
|                   | Dec. Tree |  MLP  |
|-------------------|:---------:|:-----:|
| Aedes aegypti-sex |     22    |  9033 |
| Asfault-roads     |     9     | 14833 |
| Asfault-streets   |     9     | 15176 |
| GasSensorArray    |     30    | 29660 |
| PenDigits         |     23    |  4209 |
| HAR               |     12    |   -   |


#### MK66FX1M0VMD18
|                   | Dec. Tree |  MLP |
|-------------------|:---------:|:----:|
| Aedes aegypti-sex |     2     |  355 |
| Asfault-roads     |     2     |  553 |
| Asfault-streets   |     2     |  565 |
| GasSensorArray    |     5     | 1065 |
| PenDigits         |     4     |  184 |
| HAR               |     2     | 5563 |
