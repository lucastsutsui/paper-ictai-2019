The tables below show maximum classification time (in microseconds) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  3160 |     96    | 26640 |    1616   |
| Asfault-roads     | 10776 |    120    |   -   |    5632   |
| Asfault-streets   | 15844 |    104    |   -   |    9516   |
| GasSensorArray    |   -   |    152    |   -   |   18888   |
| PenDigits         |  7644 |     -     |  8388 |   19944   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  3036 |     60    | 26780 |    1464   |
| Asfault-roads     | 11436 |     72    |   -   |    5792   |
| Asfault-streets   | 16664 |     64    |   -   |    8280   |
| GasSensorArray    |   -   |     96    |   -   |   18756   |
| PenDigits         |  7708 |     -     |  5716 |   10948   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  2080 |     44    | 10472 |    668    |
| Asfault-roads     |  5216 |     56    |   -   |    2488   |
| Asfault-streets   |  6904 |     52    |   -   |    3180   |
| GasSensorArray    | 17796 |     72    |   -   |    7288   |
| PenDigits         |  3108 |     68    |  2872 |    4160   |
| HAR               |   -   |     64    |   -   |     -     |


#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  337  |     22    |  4093 |    259    |
| Asfault-roads     |  1112 |     23    |  8179 |    1150   |
| Asfault-streets   |  1576 |     19    |  8321 |    1768   |
| GasSensorArray    |  4809 |     28    | 25097 |    3173   |
| PenDigits         |  835  |     25    |  1722 |    5427   |
| HAR               | 20018 |     24    |   -   |    7719   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex |  125 |     9     |  618 |     62    |
| Asfault-roads     |  271 |     7     | 1269 |    193    |
| Asfault-streets   |  341 |     7     | 1286 |    273    |
| GasSensorArray    |  846 |     11    | 4187 |    542    |
| PenDigits         |  151 |     9     |  179 |    383    |
| HAR               | 3681 |     9     |   -  |    2033   |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex |  40  |     9     |  431 |     52    |
| Asfault-roads     |  142 |     8     |  955 |    167    |
| Asfault-streets   |  215 |     7     |  966 |    218    |
| GasSensorArray    |  597 |     10    | 3413 |    473    |
| PenDigits         |  139 |     10    |  125 |    308    |
| HAR               | 2613 |     9     |   -  |    1836   |


#### MK66FX1M0VMD18  (floating-point representation)
|                   | SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:---:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  13 |     3     |  575  |     55    |
| Asfault-roads     |  38 |     3     |  992  |    237    |
| Asfault-streets   |  53 |     4     |  1016 |    383    |
| GasSensorArray    | 143 |     5     |  2099 |    588    |
| PenDigits         |  34 |     4     |  398  |    1504   |
| HAR               | 614 |     4     | 21546 |    809    |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  38  |     3     |  225  |     21    |
| Asfault-roads     |  93  |     3     |  488  |     72    |
| Asfault-streets   |  121 |     3     |  493  |    101    |
| GasSensorArray    |  308 |     4     |  1670 |    207    |
| PenDigits         |  59  |     4     |   58  |    129    |
| HAR               | 1334 |     3     | 25411 |    801    |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  14  |     3     |  162  |     17    |
| Asfault-roads     |  57  |     3     |  372  |     65    |
| Asfault-streets   |  86  |     3     |  377  |     86    |
| GasSensorArray    |  236 |     3     |  1365 |    186    |
| PenDigits         |  56  |     4     |   43  |    108    |
| HAR               | 1049 |     3     | 24142 |    733    |
