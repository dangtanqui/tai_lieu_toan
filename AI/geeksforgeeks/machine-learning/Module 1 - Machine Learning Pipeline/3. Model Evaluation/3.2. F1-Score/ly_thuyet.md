F1 Score is a metric used to evaluate the performance of a classification model. It combines precision and recall into a single value and is especially useful when the dataset has imbalanced classes.

*   Combines precision and recall into one metric.
*   Useful for imbalanced datasets.
*   Higher F1 Score means better performance.

![f1_score](https://media.geeksforgeeks.org/wp-content/uploads/20260313122802030936/f1_score.webp "Click to enlarge")

F1 Score is a balance between Precision and Recall

Prerequisites
-------------

### 1\. Confusion Matrix

A [confusion matrix](https://www.geeksforgeeks.org/machine-learning/confusion-matrix-machine-learning/) is a table used to evaluate the performance of a classification model. It compares the actual labels with the predicted labels to show how many predictions were correct or incorrect.

*   ****True Positive (TP):**** The model correctly predicts the positive class.
*   ****True Negative (TN):**** The model correctly predicts the negative class.
*   ****False Positive (FP):**** The model predicts positive, but the actual class is negative.
*   ****False Negative (FN):**** The model predicts negative, but the actual class is positive.

### 2\. Precision

[Precision](https://www.geeksforgeeks.org/r-language/precision-recall-and-f1-score-using-r/) measures how many of the positive predictions made by the model are actually correct. It tells us how accurate the model is when it predicts a positive class.

> Precision\=True PositivesTrue Positives+False Positives\\text{Precision} = \\frac{\\text{True Positives}}{\\text{True Positives} + \\text{False Positives}}Precision\=True Positives+False PositivesTrue Positives​

****For example:**** Suppose a model predicts 5 cases as positive. Out of these, 4 are actually positive and 1 is negative. In this case, the precision is 80% (4/5).

### 3\. Recall

Recall, also known as Sensitivity or True Positive Rate, measures how many of the actual positive cases were correctly identified by the model. It focuses on the model’s ability to detect positive instances.

> Recall\=True PositivesTrue Positives+False Negatives\\text{Recall} = \\frac{\\text{True Positives}}{\\text{True Positives} + \\text{False Negatives}}Recall\=True Positives+False NegativesTrue Positives​

****For example:**** Suppose there are 10 actual positive cases in the dataset. If the model correctly identifies 4 of them as positive, the recall becomes 40% (4/10). This means the model detected only a portion of the actual positive cases.

Combining Precision and Recall
------------------------------

F1 Score combines precision and recall into a single metric using the harmonic mean. It helps evaluate a model by balancing both precision and recall.

> F1 Score\=2×Precision×RecallPrecision+RecallF\_1 \\text{ Score} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}}F1​ Score\=2×Precision+RecallPrecision×Recall​

The F1 score becomes high only when both precision and recall are high. If either of them decreases significantly, the F1 score will also decrease.

Why Harmonic Mean is Used
-------------------------

The [harmonic mean](https://www.geeksforgeeks.org/maths/harmonic-mean/) is used instead of a simple average because it balances precision and recall more effectively. It ensures that both values need to be high for the F1 score to be high.

*   ****Balances both metrics:**** Gives equal importance to precision and recall.
*   ****Penalizes low values:**** If either precision or recall is low, the F1 score also becomes low.
*   ****Useful for imbalanced data:**** Helps evaluate models when one class appears more often than others.

Calculating F1 Score
--------------------

The F1 Score can be calculated for both binary classification and multiclass classification problems.

### 1\. Binary Classification

In [binary classification](https://www.geeksforgeeks.org/machine-learning/getting-started-with-classification/) , there are only two classes: positive and negative. The F1 score is calculated using values from the confusion matrix, which helps determine metrics like precision and recall.

****For example:**** Consider a dataset with 100 total cases. Out of these, 90 are positive and 10 are negative. The model predicts 85 cases as positive, where 80 are actually positive and 5 are actually negative. The confusion matrix would look like:

Example

Actual

Total

  

Model Prediction

80

5

85

10

5

15

Total

90

10

100

From this matrix we can calculate:

1.  ****Precision**** \= 80 / 85 = 0.94
2.  ****Recall**** \= 80 / 90 = 0.88
3.  ****Accuracy**** \= (80 + 5) / 100 = 0.85
4.  ****F1 Score**** = 0.91

This shows that the model performs well because both precision and recall are high.

### 2\. Multiclass Classification

In a [multi-class classification](https://www.geeksforgeeks.org/machine-learning/multiclass-classification-using-scikit-learn/) , where there are more than two classes, the F1 score is calculated separately for each class instead of using a single score for the whole model. This is commonly done using the One-vs-Rest (OvR) or One-vs-All (OvA) approach. The process works as follows:

*   ****Treat one class as positive:**** For each class, consider it as the positive class and all other classes as negative.
*   ****Calculate metrics per class:**** Compute precision, recall and F1 score using TP, FP and FN for that class.
*   ****Repeat for all classes:**** Perform the same calculation for every class in the dataset.
*   ****Combine the results:**** The individual F1 scores can be combined using micro-average, macro-average or weighted-average to get an overall performance measure.

Implementing F1 Score in Python
-------------------------------

We can easily calculate the F1 score in Python using the f1\_score function from the sklearn.metrics module. This function supports both binary and multiclass classification. The f1\_score function mainly uses the following parameters:

*   ****y\_true:**** The actual class labels of the dataset.
*   ****y\_pred:**** The predicted labels generated by the model.
*   ****average (optional):**** Specifies how the F1 score should be calculated when dealing with multiclass or multilabel problems.

Python`from sklearn.metrics import f1_score  y_true = [0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0] y_pred = [0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1]  f1_per_class = f1_score(y_true, y_pred, average=None) f1_micro = f1_score(y_true, y_pred, average='micro') f1_macro = f1_score(y_true, y_pred, average='macro') f1_weighted = f1_score(y_true, y_pred, average='weighted')  print("F1 score per class:", f1_per_class) print("Micro-average F1 score:", f1_micro) print("Macro-average F1 score:", f1_macro) print("Weighted-average F1 score:", f1_weighted)`

from sklearn.metrics import f1\_score

​

y\_true \= \[0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0\]

y\_pred \= \[0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1\]

​

f1\_per\_class \= f1\_score(y\_true, y\_pred, average\=None)

f1\_micro \= f1\_score(y\_true, y\_pred, average\='micro')

f1\_macro \= f1\_score(y\_true, y\_pred, average\='macro')

f1\_weighted \= f1\_score(y\_true, y\_pred, average\='weighted')

​

print("F1 score per class:", f1\_per\_class)

print("Micro-average F1 score:", f1\_micro)

print("Macro-average F1 score:", f1\_macro)

print("Weighted-average F1 score:", f1\_weighted)

****Output:****

![Implementation-of-F1-Score](https://media.geeksforgeeks.org/wp-content/uploads/20250508135804102579/Implementation-of-F1-Score.png "Click to enlarge")

Implementation of F1 Score

> *   ****Micro-average****: Calculates metrics globally by counting the total true positives, false negatives and false positives.
> *   ****Macro-average****: Averages the F1 score for each class without considering class imbalance.
> *   ****Weighted-average****: Considers class imbalance by weighting the F1 scores by the number of true instances for each class.

Suggested Quiz
----------

When is the F1 Score particularly useful?

*   A
    
    When only accuracy matters
    
*   B
    
    In regression problems
    
*   C
    
    When there is class imbalance
    
*   D
    
    When classes are balanced
    

Why is the F1 Score preferred over simple accuracy in imbalanced datasets?

*   A
    
    Because it ignores false negatives
    
*   B
    
    Because it considers only true positives
    
*   C
    
    Because it balances precision and recall using the harmonic mean
    
*   D
    
    Because it uses the arithmetic mean of all metrics
    

In multiclass classification, how is the F1 Score for each class typically computed?

*   A
    
    By comparing all classes at once
    
*   B
    
    By treating each class as positive and the rest as negative (OvR)
    
*   C
    
    By ignoring false positives
    
*   D
    
    By averaging the confusion matrices of all classes  
