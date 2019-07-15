#### Accuracies (%) in test set for the scikit-learn models running in a microcontroller with floating-point representation
|                |  SVM  |  Dec. Tree  |  MLP  | Log. Reg |
|----------------|:-----:|:-----:|:-----:|:--------:|
| Aedes aegypti-sex | 90.51 | 98.53 | 95.96 |   98.18  |
| Asfault-roads     | 92.11 | 86.13 | 92.46 |   90.97  |
| Asfault-streets   | 88.83 | 84.02 | 91.41 |   84.19  |
| GasSensorArray    | 80.02 | 97.03 | 96.43 |   98.06  |
| PenDigits         | 36.74 | 83.83 | 89.96 |   71.51  |
| HAR               | 98.58 | 93.20 | 98.54 |   98.25  |

#### Accuracies (%) in test set for the mscikit-learn models running in a microcontroller with fixed-point Q21.10 representation
|                   |  SVM  |  Dec. Tree  |  MLP  | Log. Reg. |
|-------------------|:-----:|:-----:|:-----:|:--------:|
| Aedes aegypti-sex | 86.64 | 98.49 | 96.13 |   98.15  |
| Asfault-roads     | 92.18 | 85.78 | 92.60 |   90.90  |
| Asfault-streets   | 88.92 | 84.28 | 91.84 |   84.11  |
| GasSensorArray    | 35.27 | 97.03 | 96.26 |   46.17  |
| PenDigits         | 36.41 | 83.83 | 89.87 |   71.75  |
| HAR               | 98.58 | 92.85 | 98.38 |   98.28  |

#### Accuracies (%) in test set for the scikit-learn models running in a microcontroller with fixed-point Q11.4 representation
|                   |  SVM  |  Dec. Tree  |  MLP  | Log. Reg. |
|-------------------|:-----:|:-----:|:-----:|:--------:|
| Aedes aegypti-sex | 50.00 | 70.46 | 56.44 |   50.00  |
| Asfault-roads     | 91.82 | 81.37 |  5.12 |   90.90  |
| Asfault-streets   | 83.08 | 63.06 | 64.09 |   83.42  |
| GasSensorArray    | 18.45 | 61.00 | 16.67 |   18.45  |
| PenDigits         |  9.59 | 83.83 | 57.77 |   40.38  |
| HAR               | 48.35 | 75.18 | 38.32 |   98.12  |
