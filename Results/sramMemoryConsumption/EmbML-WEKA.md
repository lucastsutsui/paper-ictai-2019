The tables below show SRAM memory consumption (in bytes) for EmbML's classifiers running with each combination of microcontroller, dataset and classification models. In some cases, it was impossible to run the classifier due to the limitation of memory imposed by the microcontroler.

#### ATmega2560  (floating-point representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  1754 |    2410   |  7002 |    1488   |
| Asfault-roads     |  3416 |    2858   |   -   |    2230   |
| Asfault-streets   |  4462 |    3256   |   -   |    2492   |
| GasSensorArray    |   -   |    4420   |   -   |    4422   |
| PenDigits         |  2826 |     -     |  2354 |    1434   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q21.10 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  1754 |    2410   |  7002 |    1488   |
| Asfault-roads     |  3416 |    2858   |   -   |    2230   |
| Asfault-streets   |  4462 |    3256   |   -   |    2492   |
| GasSensorArray    |   -   |    4420   |   -   |    4422   |
| PenDigits         |  2826 |     -     |  2354 |    1434   |
| HAR               |   -   |     -     |   -   |     -     |

#### ATmega2560  (fixed-point Q11.4 representation)
|                   |  SVM  | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:-----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex |  1410 |    2062   |  4620 |    1316   |
| Asfault-roads     |  2246 |    2386   |   -   |    1710   |
| Asfault-streets   |  2772 |    2696   |   -   |    1842   |
| GasSensorArray    |  5736 |    3532   |   -   |    2874   |
| PenDigits         |  1962 |    7606   |  1844 |    1254   |
| HAR               |   -   |    4344   |   -   |     -     |


#### MK20DX256VLH7  (floating-point representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4352 |    4336   | 4616 |    4344   |
| Asfault-roads     | 4456 |    4424   | 4856 |    4432   |
| Asfault-streets   | 4464 |    4424   | 4864 |    4432   |
| GasSensorArray    | 4728 |    4680   | 5516 |    4688   |
| PenDigits         | 4280 |    4200   | 4356 |    4208   |
| HAR               | 6460 |    6412   |   -  |    6420   |

#### MK20DX256VLH7  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4352 |    4336   | 4608 |    4336   |
| Asfault-roads     | 4456 |    4424   | 4848 |    4424   |
| Asfault-streets   | 4464 |    4424   | 4856 |    4424   |
| GasSensorArray    | 4728 |    4680   | 5508 |    4680   |
| PenDigits         | 4280 |    4200   | 4348 |    4200   |
| HAR               | 6452 |    6404   |   -  |    6404   |

#### MK20DX256VLH7  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4268 |    4252   | 4388 |    4252   |
| Asfault-roads     | 4328 |    4296   | 4508 |    4296   |
| Asfault-streets   | 4336 |    4296   | 4512 |    4296   |
| GasSensorArray    | 4472 |    4424   | 4840 |    4424   |
| PenDigits         | 4264 |    4184   | 4260 |    4184   |
| HAR               | 5328 |    5280   |   -  |    5280   |


#### MK66FX1M0VMD18  (floating-point representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 4736 |    4720   |  5000 |    4728   |
| Asfault-roads     | 4832 |    4800   |  5232 |    4808   |
| Asfault-streets   | 4840 |    4800   |  5240 |    4808   |
| GasSensorArray    | 5104 |    5056   |  5892 |    5064   |
| PenDigits         | 4664 |    4584   |  4740 |    4592   |
| HAR               | 6836 |    6788   | 10220 |    6796   |

#### MK66FX1M0VMD18  (fixed-point Q21.10 representation)
|                   |  SVM | Dec. Tree |  MLP  | Log. Reg. |
|-------------------|:----:|:---------:|:-----:|:---------:|
| Aedes aegypti-sex | 4736 |    4720   |  4992 |    4720   |
| Asfault-roads     | 4832 |    4800   |  5224 |    4800   |
| Asfault-streets   | 4840 |    4800   |  5232 |    4800   |
| GasSensorArray    | 5104 |    5056   |  5884 |    5056   |
| PenDigits         | 4664 |    4584   |  4732 |    4584   |
| HAR               | 6836 |    6788   | 10212 |    6788   |

#### MK66FX1M0VMD18  (fixed-point Q11.4 representation)
|                   |  SVM | Dec. Tree |  MLP | Log. Reg. |
|-------------------|:----:|:---------:|:----:|:---------:|
| Aedes aegypti-sex | 4652 |    4636   | 4772 |    4636   |
| Asfault-roads     | 4704 |    4672   | 4884 |    4672   |
| Asfault-streets   | 4712 |    4672   | 4888 |    4672   |
| GasSensorArray    | 4848 |    4800   | 5216 |    4800   |
| PenDigits         | 4648 |    4568   | 4644 |    4568   |
| HAR               | 5720 |    5664   | 7384 |    5672   |
