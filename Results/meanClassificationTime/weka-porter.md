The tables below show mean classification time (in microseconds) for weka-porter's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560
|                   |   J48  |
|-------------------|:------:|
| Aedes aegypti-sex |  72.67 |
| Asfault-roads     |  80.43 |
| Asfault-streets   | 101.75 |
| GasSensorArray    | 150.21 |
| PenDigits         |  75.41 |
| HAR               | 187.98 |


#### MK20DX256VLH7
|                   |  J48  |
|-------------------|:-----:|
| Aedes aegypti-sex | 12.37 |
| Asfault-roads     | 12.02 |
| Asfault-streets   | 13.59 |
| GasSensorArray    | 18.52 |
| PenDigits         | 16.74 |
| HAR               | 18.26 |


#### MK66FX1M0VMD18
|                   |  J48 |
|-------------------|:----:|
| Aedes aegypti-sex | 1.55 |
| Asfault-roads     | 1.45 |
| Asfault-streets   | 2.05 |
| GasSensorArray    | 3.26 |
| PenDigits         | 1.36 |
| HAR               | 4.33 |
