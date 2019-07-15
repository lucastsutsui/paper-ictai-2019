The tables below show SRAM memory consumption (in bytes) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  1576 |    4176   | 18848 |    1576   |
| Asfault-roads     |  2364 |    4626   | 28950 |    2364   |
| Asfault-streets   |  2626 |    4864   | 29358 |    2626   |
| GasSensorArray    |  4674 |    6196   |   -   |    4674   |
| PenDigits         |  1462 |   18968   |  8754 |    1462   |
| HAR               | 16798 |    7820   |   -   |   16798   |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  1576 |    4176   | 18848 |    1576   |
| Asfault-roads     |  2364 |    4626   | 28950 |    2364   |
| Asfault-streets   |  2626 |    4864   | 29358 |    2626   |
| GasSensorArray    |  4674 |    6196   |   -   |    4674   |
| PenDigits         |  1462 |   18968   |  8754 |    1462   |
| HAR               | 16798 |    7820   |   -   |   16798   |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 1318 |    3436   |  9960 |    1318   |
| Asfault-roads     | 1714 |    3762   | 15012 |    1714   |
| Asfault-streets   | 1846 |    3948   | 15218 |    1846   |
| GasSensorArray    | 2868 |    4912   | 28344 |    2868   |
| PenDigits         | 1264 |   14980   |  4916 |    1264   |
| HAR               | 8930 |    5794   |   -   |    8930   |

#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4328 |    4328   | 4352 |    4328   |
| Asfault-roads     | 4416 |    4416   | 4432 |    4416   |
| Asfault-streets   | 4416 |    4416   | 4432 |    4416   |
| GasSensorArray    | 4672 |    4672   | 4688 |    4672   |
| PenDigits         | 4192 |    4192   | 4208 |    4192   |
| HAR               | 6404 |    6404   | 6420 |    6404   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4328 |    4328   | 4344 |    4328   |
| Asfault-roads     | 4416 |    4416   | 4432 |    4416   |
| Asfault-streets   | 4416 |    4416   | 4432 |    4416   |
| GasSensorArray    | 4672 |    4672   | 4688 |    4672   |
| PenDigits         | 4192 |    4192   | 4208 |    4192   |
| HAR               | 6404 |    6404   | 6420 |    6404   |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4244 |    4244   | 4260 |    4244   |
| Asfault-roads     | 4288 |    4288   | 4304 |    4288   |
| Asfault-streets   | 4288 |    4288   | 4304 |    4288   |
| GasSensorArray    | 4416 |    4416   | 4432 |    4416   |
| PenDigits         | 4176 |    4176   | 4192 |    4176   |
| HAR               | 5280 |    5280   | 5296 |    5280   |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4720 |    4720   | 4744 |    4720   |
| Asfault-roads     | 4808 |    4808   | 4824 |    4808   |
| Asfault-streets   | 4808 |    4808   | 4824 |    4808   |
| GasSensorArray    | 5064 |    5064   | 5072 |    5064   |
| PenDigits         | 4584 |    4584   | 4600 |    4584   |
| HAR               | 6796 |    6796   | 6804 |    6796   |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4712 |    4712   | 4728 |    4712   |
| Asfault-roads     | 4800 |    4800   | 4816 |    4800   |
| Asfault-streets   | 4800 |    4800   | 4816 |    4800   |
| GasSensorArray    | 5056 |    5056   | 5072 |    5056   |
| PenDigits         | 4576 |    4576   | 4592 |    4576   |
| HAR               | 6788 |    6788   | 6804 |    6788   |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4628 |    4628   | 4644 |    4628   |
| Asfault-roads     | 4672 |    4672   | 4688 |    4672   |
| Asfault-streets   | 4672 |    4672   | 4688 |    4672   |
| GasSensorArray    | 4800 |    4800   | 4816 |    4800   |
| PenDigits         | 4560 |    4560   | 4576 |    4560   |
| HAR               | 5664 |    5664   | 5680 |    5664   |
