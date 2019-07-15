The tables below show flash memory consumption (in bytes) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 15084 |   17308   | 33664 |   15084   |
| Asfault-roads     | 15794 |   17672   | 43128 |   15794   |
| Asfault-streets   | 16056 |   17910   | 43792 |   16056   |
| GasSensorArray    | 17850 |   18986   |   -   |   17850   |
| PenDigits         | 15016 |   32134   | 23074 |   15016   |
| HAR               | 28248 |   18882   |   -   |   28248   |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 15576 |   17812   | 34480 |   15576   |
| Asfault-roads     | 16272 |   18174   | 43630 |   16272   |
| Asfault-streets   | 16686 |   18566   | 44196 |   16686   |
| GasSensorArray    | 18328 |   19488   |   -   |   18328   |
| PenDigits         | 15372 |   32514   | 23438 |   15372   |
| HAR               | 28284 |   18930   |   -   |   28284   |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 15182 |   17096   | 24572 |   15182   |
| Asfault-roads     | 15546 |   17378   | 29342 |   15546   |
| Asfault-streets   | 15830 |   17716   | 29678 |   15830   |
| GasSensorArray    | 16568 |   18400   | 42546 |   16568   |
| PenDigits         | 14982 |   28482   | 19138 |   14982   |
| HAR               | 21772 |   18420   |   -   |   21772   |

#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 34240 |   35632   |  52840 |   34240   |
| Asfault-roads     | 34944 |   35992   |  61776 |   34944   |
| Asfault-streets   | 35208 |   36232   |  62184 |   35208   |
| GasSensorArray    | 37000 |   37304   |  88192 |   37000   |
| PenDigits         | 34272 |   50560   |  41808 |   34272   |
| HAR               | 47456 |   37264   | 261456 |   47456   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 33672 |   36208   |  52216 |   33672   |
| Asfault-roads     | 34368 |   36568   |  61136 |   34368   |
| Asfault-streets   | 34632 |   36808   |  61544 |   34632   |
| GasSensorArray    | 36424 |   37880   |  87552 |   36424   |
| PenDigits         | 33696 |   51136   |  41168 |   33696   |
| HAR               | 46816 |   37840   | 260816 |   46816   |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 33496 |   35552   |  42512 |   33496   |
| Asfault-roads     | 33848 |   35832   |  47328 |   33848   |
| Asfault-streets   | 33984 |   36016   |  47536 |   33984   |
| GasSensorArray    | 34872 |   36856   |  60536 |   34872   |
| PenDigits         | 33512 |   47160   |  37344 |   33512   |
| HAR               | 40072 |   36936   | 147200 |   40072   |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 36988 |   39660   |  55780 |   36988   |
| Asfault-roads     | 37756 |   40020   |  64596 |   37756   |
| Asfault-streets   | 38020 |   40260   |  64996 |   38020   |
| GasSensorArray    | 39812 |   41340   |  89596 |   39812   |
| PenDigits         | 37084 |   54588   |  44620 |   37084   |
| HAR               | 50204 |   41228   | 262796 |   50204   |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 35652 |   38252   |  54196 |   35652   |
| Asfault-roads     | 36348 |   38612   |  63188 |   36348   |
| Asfault-streets   | 36612 |   38852   |  63588 |   36612   |
| GasSensorArray    | 38404 |   39932   |  89596 |   38404   |
| PenDigits         | 35676 |   53180   |  43212 |   35676   |
| HAR               | 48860 |   39820   | 262796 |   48860   |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |   MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:------:|:---------:|
| Aedes aegypti-sex | 35476 |   37596   |  44500 |   35476   |
| Asfault-roads     | 35828 |   37876   |  49380 |   35828   |
| Asfault-streets   | 35964 |   38068   |  49580 |   35964   |
| GasSensorArray    | 36860 |   38900   |  62580 |   36860   |
| PenDigits         | 35492 |   49212   |  39396 |   35492   |
| HAR               | 42116 |   38916   | 149244 |   42116   |
