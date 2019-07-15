The tables below show SRAM memory consumption (in bytes) for emlearn's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   | Dec. Tree | MLP |
|-------------------|:---------:|:---:|
| Aedes aegypti-sex |    1230   |  -  |
| Asfault-roads     |    1318   |  -  |
| Asfault-streets   |    1320   |  -  |
| GasSensorArray    |    1570   |  -  |
| PenDigits         |    1090   |  -  |
| HAR               |    3302   |  -  |


#### MK20DX256VLH7
|                   | Dec. Tree |  MLP |
|-------------------|:---------:|:----:|
| Aedes aegypti-sex |    4336   | 5160 |
| Asfault-roads     |    4424   | 5248 |
| Asfault-streets   |    4424   | 5248 |
| GasSensorArray    |    4680   | 5728 |
| PenDigits         |    4200   | 5024 |
| HAR               |    6412   |   -  |


#### MK66FX1M0VMD18
|                   | Dec. Tree |  MLP  |
|-------------------|:---------:|:-----:|
| Aedes aegypti-sex |    4720   |  5544 |
| Asfault-roads     |    4808   |  5632 |
| Asfault-streets   |    4808   |  5632 |
| GasSensorArray    |    5064   |  6112 |
| PenDigits         |    4584   |  5408 |
| HAR               |    6796   | 11308 |
