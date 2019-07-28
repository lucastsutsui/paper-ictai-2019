The tables below show flash memory consumption (in bytes) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 15618 |   15550   | 21396 |   15928   |
| Asfault-roads     | 17418 |   15892   |   -   |   16742   |
| Asfault-streets   | 18484 |   16290   |   -   |   17004   |
| GasSensorArray    |   -   |   17202   |   -   |   18696   |
| PenDigits         | 17264 |     -     | 16926 |   16184   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 16562 |   16020   | 22472 |   17328   |
| Asfault-roads     | 18232 |   16382   |   -   |   18158   |
| Asfault-streets   | 19298 |   16780   |   -   |   18420   |
| GasSensorArray    |   -   |   17692   |   -   |   20254   |
| PenDigits         | 18016 |     -     | 17484 |   17120   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 15374 |   15862   | 18990 |   15864   |
| Asfault-roads     | 16462 |   15992   |   -   |   16364   |
| Asfault-streets   | 17008 |   16302   |   -   |   16506   |
| GasSensorArray    | 20006 |   17016   |   -   |   17528   |
| PenDigits         | 16392 |   21294   | 16172 |   15902   |
| HAR               |   -   |   16974   |   -   |     -     |


#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 36016 |   35272   | 42208 |   36856   |
| Asfault-roads     | 37648 |   35632   | 49280 |   37616   |
| Asfault-streets   | 38752 |   36032   | 49496 |   37872   |
| GasSensorArray    | 44424 |   36952   | 83616 |   39752   |
| PenDigits         | 37384 |   42488   | 37832 |   36928   |
| HAR               | 73864 |   36872   |   -   |   50144   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 36272 |   35848   | 41520 |   36360   |
| Asfault-roads     | 37968 |   36208   | 48592 |   37120   |
| Asfault-streets   | 39008 |   36608   | 48872 |   37376   |
| GasSensorArray    | 44680 |   37528   | 82992 |   39256   |
| PenDigits         | 37640 |   43064   | 37144 |   36432   |
| HAR               | 72776 |   36040   |   -   |   48240   |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 35120 |   35584   | 38464 |   35376   |
| Asfault-roads     | 35960 |   35864   | 42592 |   35832   |
| Asfault-streets   | 36552 |   36176   | 42736 |   35960   |
| GasSensorArray    | 39400 |   36896   | 63392 |   37008   |
| PenDigits         | 35896 |   41200   | 35832 |   35376   |
| HAR               | 52776 |   35496   |   -   |   41728   |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |  SVM  | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:-----:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex | 37356 |   37828   |  43676  |   38316   |
| Asfault-roads     | 37580 |   36780   |  49276  |   37668   |
| Asfault-streets   | 38620 |   37180   |  49548  |   37932   |
| GasSensorArray    | 44292 |   38100   |  83668  |   39748   |
| PenDigits         | 38724 |   45052   |  39300  |   38396   |
| HAR               | 73796 |   37956   | 1009548 |   50204   |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |   MLP   | Log. Reg. |
|-------------------|:-----:|:---------:|:-------:|:---------:|
| Aedes aegypti-sex | 38316 |   37892   |  43564  |   38404   |
| Asfault-roads     | 38540 |   36780   |  49228  |   37756   |
| Asfault-streets   | 39580 |   37180   |  49444  |   38012   |
| GasSensorArray    | 45316 |   38164   |  83564  |   39828   |
| PenDigits         | 39684 |   45116   |  39188  |   38484   |
| HAR               | 74756 |   38020   | 1009500 |   50220   |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 37164 |   37628   |  40508 |   37420   |
| Asfault-roads     | 36604 |   36500   |  43236 |   36468   |
| Asfault-streets   | 37124 |   36812   |  43372 |   36596   |
| GasSensorArray    | 40036 |   37532   |  64028 |   37644   |
| PenDigits         | 37948 |   43244   |  37876 |   37428   |
| HAR               | 56228 |   37476   | 686244 |   45180   |
