Feature selection is the process of choosing only the most useful input features for a machine learning model. It helps improve model performance, reduces noise and makes results easier to understand.

*   Helps remove irrelevant and redundant features
*   Improves accuracy and reduces overfitting
*   Speeds up model training
*   Makes models simpler and easier to interpret

![binary_number_system.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)![binary_number_system.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)

![1.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165146012474/1.webp)![1.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165146012474/1.webp)

![2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165145779522/2.webp)![2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250512165145779522/2.webp)

![3.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)![3.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251212172709886667/binary_number_system.webp)

Previous Pause Next 3 / 4

### Need of Feature Selection

Feature selection methods are essential in data science and machine learning for several key reasons:

*   ****Improved Accuracy****: Models learn better when trained on only important features.
*   ****Faster Training****: Fewer features reduce computation time.
*   ****Greater Interpretability****: With fewer inputs, understanding model behavior becomes easier.
*   ****Avoiding the Curse of Dimensionality****: Reduces complexity when working with high-dimensional data.

Types of Feature Selection Methods
----------------------------------

There are various algorithms used for feature selection and are grouped into three main categories and each one has its own strengths and trade-offs depending on the use case.

### 1\. Filter Methods

[Filter methods](https://www.geeksforgeeks.org/machine-learning/feature-selection-filter-methods/) evaluate each feature independently with respect to the target variable. Features are selected based on statistical measures that indicate their relevance to the target. These methods are commonly used in the preprocessing phase to remove irrelevant or redundant features.

*   Do not rely only on correlation
*   Use different statistical techniques depending on data type
*   Fast and model-independent feature selection approach

![filter](https://media.geeksforgeeks.org/wp-content/uploads/20250830103247936857/filter.webp "Click to enlarge")

Filter Method

****Common Filter Techniques****

*   [****Information Gain****](https://www.geeksforgeeks.org/machine-learning/information-gain-and-mutual-information-for-machine-learning/)****:**** Measures reduction in entropy when a feature is used.
*   [****Chi-square test****](https://www.geeksforgeeks.org/maths/chi-square-test/)****:**** Checks the relationship between categorical features.
*   [****Fisher’s Score:****](https://www.geeksforgeeks.org/r-language/fishers-f-test-in-r-programming/) Ranks features based on class separability.
*   [****Pearson’s Correlation Coefficient****](https://www.geeksforgeeks.org/maths/pearson-correlation-coefficient/)****:**** Measures linear relationship between two continuous variables.
*   [****Variance Threshold****](https://www.geeksforgeeks.org/machine-learning/variance-threshold/)****:**** Removes features with very low variance.
*   [****Mean Absolute Difference****](https://www.geeksforgeeks.org/maths/mean-absolute-deviation/)****:**** Similar to variance threshold but uses absolute differences.
*   [****Dispersion ratio****](https://www.geeksforgeeks.org/maths/measures-of-dispersion/)****:**** Ratio of arithmetic mean to geometric mean; higher values indicate useful features.

****Advantages****

*   ****Fast and efficient****: Filter methods are computationally inexpensive, making them ideal for large datasets.
*   ****Easy to implement****: These methods are often built-in to popular machine learning libraries, requiring minimal coding effort.
*   ****Model Independence****: Filter methods can be used with any type of machine learning model, making them versatile tools.

****Limitations****

*   ****Limited interaction with the model****: Since they operate independently, filter methods might miss data interactions that could be important for prediction.
*   ****Choosing the right metric****: Selecting the appropriate metric for our data and task is important for optimal performance.

### 2\. Wrapper methods

[Wrapper methods](https://www.geeksforgeeks.org/machine-learning/wrapper-methods-feature-selection/) are feature selection techniques that evaluate different combinations of features by measuring their impact on model performance. They use search strategies to add or remove features and select the optimal subset based on predefined stopping criteria.

*   Evaluates feature subsets using a machine learning model
*   Uses greedy or non-greedy search strategies
*   Measures the relationship between feature subsets and the target variable
*   Adds or removes features based on model performance
*   Stops when performance decreases or the desired number of features is reached

![wrapper](https://media.geeksforgeeks.org/wp-content/uploads/20250830104446954251/wrapper.webp "Click to enlarge")

Wrapper Method

****Common Wrapper Techniques****

*   [****Forward Selection****](https://www.geeksforgeeks.org/machine-learning/forward-feature-selection-in-machine-learning/)****:**** Start with no features and add one at a time based on improvement.
*   [****Backward Elimination****](https://www.geeksforgeeks.org/machine-learning/ml-multiple-linear-regression-backward-elimination-technique/)****:**** Start with all features and remove the least useful ones.
*   [****Recursive Feature Elimination (RFE)****](https://www.geeksforgeeks.org/machine-learning/recursive-feature-elimination/)****:**** Removes the least important features step by step.

### Advantages

*   ****Model-specific optimization****: Wrapper methods directly consider how features influence the model, potentially leading to better performance compared to filter methods.
*   ****Flexible****: These methods can be adapted to various model types and evaluation metrics.

### Limitations

*   ****Computationally expensive****: Evaluating different feature combinations can be time-consuming, especially for large datasets.
*   ****Risk of overfitting****: Fine-tuning features to a specific model can lead to an overfitted model that performs poorly on unseen data.

### 3\. Embedded methods

[Embedded methods](https://www.geeksforgeeks.org/machine-learning/feature-selection-embedded-methods/) perform feature selection during the model training process. They combine the benefits of both filter and wrapper methods. Feature selection is integrated into the model training allowing the model to select the most relevant features based on the training process dynamically.

![embedded](https://media.geeksforgeeks.org/wp-content/uploads/20250830104521819821/embedded.webp "Click to enlarge")

Embedded Method

****Common Embedded Techniques****

*   [****L1 Regularization (Lasso)****](https://www.geeksforgeeks.org/machine-learning/what-is-lasso-regression/)****:**** Keeps only features with non-zero coefficients.
*   [****Decision Trees****](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/) and [****Random Forests****](https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/)****:**** Select features based on impurity reduction.
*   [****Gradient Boosting****](https://www.geeksforgeeks.org/machine-learning/ml-gradient-boosting/)****:**** Pick features that reduce prediction error the most

****Advantages****

*   ****Efficient and effective****: Embedded methods can achieve good results without the computational burden of some wrapper methods.
*   ****Model-specific learning****: Similar to wrapper methods these techniques uses the learning process to identify relevant features.

****Limitations****

*   ****Limited interpretability****: Embedded methods can be more challenging to interpret compared to filter methods making it harder to understand why specific features were chosen.
*   ****Not universally applicable****: Not all machine learning algorithms support embedded feature selection techniques.

Choosing the Right Feature Selection Method
-------------------------------------------

Choice of feature selection method depends on several factors:

*   ****Dataset size****: Filter methods are generally faster for large datasets while wrapper methods might be suitable for smaller datasets.
*   ****Model type****: Some models like tree-based models, have built-in feature selection capabilities.
*   ****Interpretability****: If understanding the rationale behind feature selection is crucial, filter methods might be a better choice.
*   ****Computational resources:**** Wrapper methods can be time-consuming, so consider our available computing power.

With these feature selection methods we can easily improve performance of our model and reduce its computational cost.

Suggested Quiz
----------

Which of the following is a filter method for feature selection?

*   A
    
    Recursive Feature Elimination
    
*   B
    
    Chi-Square Test
    
*   C
    
    Random Forest
    
*   D
    
    Backward Elimination
    

What does a high dispersion ratio in a feature imply?  

*   A
    
    Feature is constant
    
*   B
    
    Feature is more relevant
    
*   C
    
    Feature has missing values
    
*   D
    
    Feature is irrelevant
    

In wrapper methods, which approach starts with all features and removes the least useful one in each step

*   A
    
    Backward Elimination
    
*   B
    
    Forward Selection
    
*   C
    
    Fisher’s Score
    
*   D
    
    L1 Regularization
    

What is the relationship between feature selection and the curse of dimensionality?

*   A
    
    Increases dimensionality
    
*   B
    
    Has no effect
    
*   C
    
    Reduces dimensionality and complexity
    
*   D
    
    Converts features
    

What is a limitation of filter methods?

*   A
    
    Slow execution
    
*   B
    
    High computational cost
    
*   C
    
    Requires training data
    
*   D
    
    Ignores feature interactions
