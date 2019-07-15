The tables below show mean classification time (in microseconds) for emlearn's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   | Dec. Tree | MLP |
|-------------------|:---------:|:---:|
| Aedes aegypti-sex |   55.28   |  -  |
| Asfault-roads     |   27.36   |  -  |
| Asfault-streets   |   29.77   |  -  |
| GasSensorArray    |   56.69   |  -  |
| PenDigits         |   61.41   |  -  |
| HAR               |   29.94   |  -  |


#### MK20DX256VLH7
|                   | Dec. Tree |    MLP   |
|-------------------|:---------:|:--------:|
| Aedes aegypti-sex |   11.90   |  9002.85 |
| Asfault-roads     |    4.94   | 14758.22 |
| Asfault-streets   |    5.90   | 15085.99 |
| GasSensorArray    |   11.93   | 29281.54 |
| PenDigits         |   12.70   |  4101.68 |
| HAR               |    5.97   |     -    |


#### MK66FX1M0VMD18
|                   | Dec. Tree |   MLP   |
|-------------------|:---------:|:-------:|
| Aedes aegypti-sex |    0.83   |  349.82 |
| Asfault-roads     |    0.53   |  548.57 |
| Asfault-streets   |    0.45   |  560.88 |
| GasSensorArray    |    1.11   | 1058.44 |
| PenDigits         |    1.52   |  174.33 |
| HAR               |    0.78   | 5171.48 |
