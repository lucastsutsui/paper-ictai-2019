Backup of implementations for the EmbML tool to convert WEKA or scikit-learn trained classifiers into code to run in low-cost embedded systems.

JavaObj library must be installed <https://pypi.org/project/javaobj-py3/>

### Usage: 
```
    python toolWeka/j48.py <modelFile> <destinationFile> [-opts]
    python toolWeka/logistic.py <modelFile> <destinationFile> [-opts]
    python toolWeka/mlp.py <modelFile> <destinationFile> [-opts]
    python toolWeka/svmLinear.py <modelFile> <destinationFile> [-opts]

    python toolSklearn/decisionTree.py <modelFile> <destinationFile> [-opts]
    python toolSklearn/logisticRegression.py <modelFile> <destinationFile> [-opts]
    python toolSklearn/mlpClassifier.py <modelFile> <destinationFile> [-opts]
    python toolSklearn/linearSVC.py <modelFile> <destinationFile> [-opts]
    python toolSklearn/svmKernel.py <modelFile> <destinationFile> [-opts]
```
    
*modelFile* is the WEKA or scikit-learn trained classification model

*destinationFile* is the file that will be produced containing the classifier

```
Options:	
		-fxp:  use fixed point Qn.m (n integer bits ans m fractional bits) representation in all operations
```

If fixed-point representation is used, *FixedNum.h* must be included in the same folder of the classifier file.
