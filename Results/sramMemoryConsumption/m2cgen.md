The tables below show SRAM memory consumption (in bytes) for m2cgen's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |  SVM | Dec. Tree | Log. Reg. |
|-------------------|:----:|:---------:|:---------:|
| Aedes aegypti-sex | 1230 |    1228   |    1230   |
| Asfault-roads     | 1318 |    1318   |    1318   |
| Asfault-streets   | 1320 |    1320   |    1320   |
| GasSensorArray    | 1570 |    1570   |    1570   |
| PenDigits         | 1092 |    1090   |    1092   |
| HAR               | 3302 |    3302   |    3302   |


#### MK20DX256VLH7
|                   |  SVM | Dec. Tree | Log. Reg. |
|-------------------|:----:|:---------:|:---------:|
| Aedes aegypti-sex | 4336 |    4336   |    4336   |
| Asfault-roads     | 4424 |    4424   |    4424   |
| Asfault-streets   | 4424 |    4424   |    4424   |
| GasSensorArray    | 4680 |    4680   |    4680   |
| PenDigits         | 4200 |    4200   |    4200   |
| HAR               | 6412 |    6412   |    6412   |


#### MK66FX1M0VMD18
|                   |  SVM | Dec. Tree | Log. Reg. |
|-------------------|:----:|:---------:|:---------:|
| Aedes aegypti-sex | 4712 |    4712   |    4712   |
| Asfault-roads     | 4800 |    4800   |    4800   |
| Asfault-streets   | 4800 |    4800   |    4800   |
| GasSensorArray    | 5056 |    5056   |    5056   |
| PenDigits         | 4576 |    4576   |    4576   |
| HAR               | 6788 |    6788   |    6788   |
