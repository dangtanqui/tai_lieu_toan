Hyperparameter tuning is the process of selecting the optimal values for a machine learning model's hyperparameters. These are typically set before the actual training process begins and control aspects of the learning process itself. Effective tuning helps the model learn better patterns, avoid overfitting or underfitting and achieve higher accuracy on unseen data.

Techniques for Hyperparameter Tuning
------------------------------------

Models can have many hyperparameters and finding the best combination of parameters can be treated as a search problem. The two best strategies for Hyperparameter tuning are:

![397349273.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251222173603532083/397349273.webp)![397349273.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251222173603532083/397349273.webp)

![397349272.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103915201685/397349272.webp)![397349272.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103915201685/397349272.webp)

![397349274.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103914899123/397349274.webp)![397349274.webp](https://media.geeksforgeeks.org/wp-content/uploads/20251216103914899123/397349274.webp)

Previous Pause Next 1 / 3

### ****1\. GridSearchCV**** 

[GridSearchCV](https://www.geeksforgeeks.org/machine-learning/performing-feature-selection-with-gridsearchcv-in-sklearn/) is a brute-force technique for hyperparameter tuning. It trains the model using all possible combinations of specified hyperparameter values to find the best-performing setup. It is slow and uses a lot of computer power which makes it hard to use with big datasets or many settings. It works using below steps:

*   Create a grid of potential values for each hyperparameter.
*   Train the model for every combination in the grid.
*   Evaluate each model using cross-validation.
*   Select the combination that gives the highest score.

For example if we want to tune two [hyperparameters](https://www.geeksforgeeks.org/machine-learning/how-to-optimize-logistic-regression-performance/) C and penalty for a [Logistic Regression Classifier](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/) model with the following sets of values:  
C = \[0.1, 0.2, 0.3, 0.4, 0.5\]  
penalty = \[0.01, 0.1, 0.5, 1.0\]

![GridSearchCV](https://media.geeksforgeeks.org/wp-content/uploads/Hyp_tune.png "Click to enlarge")

The grid search technique will construct multiple versions of the model with all possible combinations of C and Alpha, resulting in a total of 5 \* 4 = 20 different models. The best-performing combination is then chosen.

****Example:**** Tuning Logistic Regression with GridSearchCV

The following code illustrates how to use GridSearchCV . In this below code:

*   We generate sample data using make\_classification.
*   We define a range of `C` values using logarithmic scale.
*   GridSearchCV tries all combinations from param\_grid and uses 5-fold cross-validation.
*   It returns the best hyperparameter (`C`) and its corresponding validation score

Python`from sklearn.linear_model import LogisticRegression from sklearn.model_selection import GridSearchCV import numpy as np from sklearn.datasets import make_classification  X, y = make_classification(     n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)  c_space = np.logspace(-5, 8, 15)  param_grid = {     'C': c_space,     'penalty': ['l1', 'l2'] }  logreg = LogisticRegression(solver='liblinear')  logreg_cv = GridSearchCV(logreg, param_grid, cv=5)  logreg_cv.fit(X, y)  print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_)) print("Best score is {}".format(logreg_cv.best_score_))`

****Output:****

> Tuned Logistic Regression Parameters: {'C': 0.006105402296585327}  
> Best score is 0.853

This represents the highest accuracy achieved by the model using the hyperparameter combination C = 0.0061. The best score of 0.853 means the model achieved 85.3% accuracy on the validation data during the grid search process.

### ****2\. RandomizedSearchCV**** 

As the name suggests [RandomizedSearchCV](https://www.geeksforgeeks.org/machine-learning/comparing-randomized-search-and-grid-search-for-hyperparameter-estimation-in-scikit-learn/) picks random combinations of hyperparameters from the given ranges instead of checking every single combination like GridSearchCV.

*   In each iteration it tries a new random combination of hyperparameter values.
*   It records the model’s performance for each combination.
*   After several attempts it selects the best-performing set.

****Example:**** Tuning Decision Tree with RandomizedSearchCV

The following code illustrates how to use RandomizedSearchCV. In this example:

*   We define a range of values for each [hyperparameter](https://www.geeksforgeeks.org/machine-learning/how-to-tune-a-decision-tree-in-hyperparameter-tuning/) e.g, max\_depth, min\_samples\_leaf etc.
*   Random combinations are picked and evaluated using 5-fold cross-validation.
*   The best combination and score are printed.

Python`import numpy as np from sklearn.datasets import make_classification  X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_classes=2, random_state=42)  from scipy.stats import randint from sklearn.tree import DecisionTreeClassifier from sklearn.model_selection import RandomizedSearchCV  param_dist = {     "max_depth": [3, None],     "max_features": randint(1, 9),     "min_samples_leaf": randint(1, 9),     "criterion": ["gini", "entropy"] }  tree = DecisionTreeClassifier() tree_cv = RandomizedSearchCV(tree, param_dist, cv=5) tree_cv.fit(X, y)  print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_)) print("Best score is {}".format(tree_cv.best_score_))`

****Output:****

> Tuned Decision Tree Parameters: {'criterion': 'entropy', 'max\_depth': None, 'max\_features': 6, 'min\_samples\_leaf': 6}  
> Best score is 0.8

A score of 0.842 means the model performed with an accuracy of 84.2% on the validation set with following hyperparameters.

### ****3\. Bayesian Optimization****

Grid Search and Random Search can be inefficient because they blindly try many hyperparameter combinations, even if some are clearly not useful. [Bayesian Optimization](https://www.geeksforgeeks.org/artificial-intelligence/bayesian-optimization-in-machine-learning/) takes a smarter approach. It treats hyperparameter tuning like a mathematical optimization problem and learns from past results to decide what to try next.

*   Build a probabilistic model (surrogate function) that predicts performance based on hyperparameters.
*   Update this model after each evaluation.
*   Use the model to choose the next best set to try.
*   Repeat until the optimal combination is found. The surrogate function models:

> P(score(y)∣hyperparameters(x))P(\\text{score}(y) \\mid \\text{hyperparameters}(x))P(score(y)∣hyperparameters(x))

Here the surrogate function models the relationship between hyperparameters xxx and the score yyy. By updating this model iteratively with each new evaluation Bayesian optimization makes more informed decisions. Common surrogate models used in Bayesian optimization include:

*   Gaussian Processes
*   Random Forest Regression
*   Tree-structured Parzen Estimators (TPE)

****Advantages****
------------------

*   Finding the optimal combination of hyperparameters can significantly boost model accuracy and robustness.
*   Tuning helps prevent both overfitting and underfitting, resulting in a well-balanced model.
*   By selecting hyperparameters that perform well on validation data, the model can generalize better to unseen data.
*   It also helps in using computational resources like time and memory more efficiently by avoiding unnecessary trials.
*   Proper tuning can make the model simpler and easier to understand and interpret.

****Challenges****
------------------

*   Larger hyperparameter spaces increase the number of combinations to explore, making the process computationally expensive and time-consuming, especially for complex models.
*   Using prior knowledge helps narrow the search space, improving both efficiency and effectiveness of hyperparameter tuning.
*   Dynamically adjusting hyperparameters during training, such as learning rate scheduling or early stopping, can improve model performance.

Suggested Quiz
----------

What is the main goal of hyperparameter tuning?  

*   A
    
    Reducing training time
    
*   B
    
    Increasing dataset size
    
*   C
    
    Changing model parameters after training
    
*   D
    
    Improving model performance by optimizing hyperparameters
    

What is the main difference between GridSearchCV and RandomizedSearchCV?

*   A
    
    GridSearchCV selects hyperparameters randomly, while RandomizedSearchCV checks all combinations
    
*   B
    
    GridSearchCV only works for Decision Trees
    
*   C
    
    Both perform exhaustive search  
    
*   D
    
    GridSearchCV tests every possible combination, while RandomizedSearchCV tries random combinations
    

Imagine you are tuning a model with 50 hyperparameters. GridSearchCV would require testing millions of combinations. Which tuning method would most efficiently explore this huge search space while learning from previous trials?

*   A
    
    Holdout Validation
    
*   B
    
    K-Fold Cross Validation
    
*   C
    
    RandomizedSearchCV
    
*   D
    
    Bayesian Optimization
    

At what stage of the machine learning workflow are hyperparameters typically defined?

*   A
    
    Before the training process begins
    
*   B
    
    After model evaluation
    
*   C
    
    During prediction
    
*   D
    
    After feature selection
    

What is the key advantage of Bayesian Optimization over Grid Search and Random Search?

*   A
    
    It avoids cross-validation
    
*   B
    
    It uses fewer hyperparameters
    
*   C
    
    It learns from previous evaluations to guide future searches
    
*   D
    
    It tests all combinations faster
