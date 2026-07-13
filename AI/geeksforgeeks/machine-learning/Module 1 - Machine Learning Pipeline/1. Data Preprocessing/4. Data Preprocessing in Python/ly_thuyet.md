Data preprocessing is the first step in any data analysis or machine learning pipeline. It involves cleaning, transforming and organizing raw data to ensure it is accurate, consistent and ready for modeling. It has a big impact on model building such as:

*   Clean and well-structured data allows models to learn meaningful patterns rather than noise.
*   Properly processed data prevents misleading inputs, leading to more reliable predictions.
*   Organized data makes it simpler to create useful inputs for the model, enhancing model performance.
*   Organized data supports better Exploratory Data Analysis (EDA), making patterns and trends more interpretable.

![data_cleaning](https://media.geeksforgeeks.org/wp-content/uploads/20251212113640777958/data_cleaning.webp "Click to enlarge")

Steps-by-Step implementation
----------------------------

Let's implement various preprocessing features,

### Step 1: Import Libraries and Load Dataset

We prepare the environment with libraries like [pandas](https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/), [numpy](https://www.geeksforgeeks.org/numpy/python-numpy/), [scikit learn](https://www.geeksforgeeks.org/machine-learning/learning-model-building-scikit-learn-python-machine-learning-library/), [matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) and [seaborn](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) for data manipulation, numerical operations, visualization and scaling. Load the dataset for preprocessing.

> The sample dataset can be downloaded from [here](https://media.geeksforgeeks.org/wp-content/uploads/20250115110111213229/diabetes.csv).

```python
import pandas as pd
import numpy as np from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Geeksforgeeks/Data/diabetes.csv')
df.head()
```

****Output:****

![Screenshot-2025-08-29-132400](https://media.geeksforgeeks.org/wp-content/uploads/20250829133434412896/Screenshot-2025-08-29-132400.webp "Click to enlarge")

### Step 2: Inspect Data Structure and Check Missing Values

We understand dataset size, data types and identify any incomplete (missing) data that needs handling.

*   ****df.info():**** Prints concise summary including count of non-null entries and data type of each column.
*   ****df.isnull().sum():**** Returns the number of missing values per column.

```python
df.info()
print(df.isnull().sum())
```

****Output:****

![Screenshot-2025-08-29-132349.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133538216025/Screenshot-2025-08-29-132349.webp)

![Screenshot-2025-08-29-132333.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133538354485/Screenshot-2025-08-29-132333.webp)

### Step 3: Statistical Summary and Visualizing Outliers

Get numeric summaries like mean, median, min/max and detect unusual points (outliers). Outliers can skew models if not handled.

*   ****df.describe():**** Computes count, mean, std deviation, min/max and quartiles for numerical columns.
*   ****Boxplots:**** Visualize spread and detect outliers using matplotlib’s boxplot().

```python
df.describe()
fig, axs = plt.subplots(len(df.columns), 1, figsize=(7, 18), dpi=95) for i, col in enumerate(df.columns):
axs[i].boxplot(df[col], vert=False)
axs[i].set_ylabel(col)
plt.tight_layout()
plt.show()
```

****Output:****

![boxplot-data-preprocessing](https://media.geeksforgeeks.org/wp-content/uploads/20250829133635752868/boxplot-data-preprocessing.webp "Click to enlarge")

### Step 4: Remove Outliers Using the Interquartile Range (IQR) Method

Remove extreme values beyond a reasonable range to improve model robustness.

*   IQR = Q3 (75th percentile) – Q1 (25th percentile).
*   Values below Q1 - 1.5IQR or above Q3 + 1.5IQR are outliers.
*   Calculate lower and upper bounds for each column separately.
*   Filter data points to keep only those within bounds.

```python
q1, q3 = np.percentile(df['Insulin'], [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
clean_df = df[(df['Insulin'] >= lower) & (df['Insulin'] <= upper)]
```

> ****Note:**** In practice, outlier removal should be applied across all relevant numerical columns to ensure consistent preprocessing.

### Step 5: Correlation Analysis

Understand relationships between features and the target variable (Outcome). Correlation helps gauge feature importance.

*   ****df.corr():**** Computes pairwise correlation coefficients between columns.
*   Heatmap via seaborn visualizes correlation matrix clearly.
*   Sorting correlations with corr\['Outcome'\].sort\_values() highlights features most correlated with the target.

```python
corr = df.corr()
plt.figure(dpi=130)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.show()
print(corr['Outcome'].sort_values(ascending=False))
```

****Output:****

![seashore.webp](https://media.geeksforgeeks.org/wp-content/uploads/20250829133737344121/seashore.webp)

### Step 6: Visualize Target Variable Distribution

Check if target classes (Diabetes vs Not Diabetes) are balanced, affecting model training and evaluation.

*   ****plt.pie():**** Pie chart to display proportion of each class in the target variable 'Outcome'.

```python
plt.pie(clean_df['Outcome'].value_counts(),
labels=['Diabetes', 'Not Diabetes'],
autopct='%.f%%', shadow=True)
plt.title('Outcome Proportionality')
plt.show()
```

****Output:****

![pie](https://media.geeksforgeeks.org/wp-content/uploads/20250829133842061194/pie.webp "Click to enlarge")

### Step 7: Separate Features and Target Variable

Prepare independent variables (features) and dependent variable (target) separately for modeling.

*   ****df.drop(columns=\[...\]):**** Drops the target column from features.
*   Direct column selection df\['Outcome'\] selects target column.

```python
X = df.drop(columns=['Outcome'])
y = df['Outcome']
```

### Step 8: Feature Scaling: Normalization and Standardization

Scale features to a common range or distribution, important for many ML algorithms sensitive to feature magnitudes.

****1\. Normalization (Min-Max Scaling):**** Rescales features between 0 and 1. Good for algorithms like k-NN and neural networks.

*   ****Class:**** MinMaxScaler from sklearn.
*   ****.fit\_transform():**** Learns min/max from data and applies scaling.

```python
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
print(X_normalized[:5])
```

****Output:****

![Screenshot-2025-08-29-132258](https://media.geeksforgeeks.org/wp-content/uploads/20250829133922543007/Screenshot-2025-08-29-132258.webp "Click to enlarge")

****2\. Standardization:**** Transforms features to have mean = 0 and standard deviation = 1, useful for normally distributed features.

*   ****Class:**** StandardScaler from sklearn.

```python
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
print(X_standardized[:5])
```

****Output:****

![Screenshot-2025-08-29-132251](https://media.geeksforgeeks.org/wp-content/uploads/20250829134002498787/Screenshot-2025-08-29-132251.webp "Click to enlarge")

Advantages
----------

*   Cleans and organizes raw data for better analysis.
*   Removes noise and irrelevant data, leading to more precise predictions.
*   Handles outliers and redundant features, which reduces overfitting.
*   Scaling data helps models train faster by reducing computation time.
*   Converts data into formats suitable for machine learning models.

Suggested Quiz
----------

What is the main purpose of data preprocessing?

- [ ] A. Deploying the model
    
- [ ] B. Cleaning, transforming and organizing raw data
    
- [ ] C. Increasing dataset size
    
- [ ] D. Visualizing only the target variable
    

Which function helps identify missing values in each column?

- [ ] A. df.describe()
    
- [ ] B. B. df.info()
    
- [ ] C. df.isnull().sum()
    
- [ ] D. df.corr()
    

In the IQR method, outliers are values that:

- [ ] A. Are equal to the median
    
- [ ] B. Are greater than the mean
    
- [ ] C. Fall below Q1 − 1.5IQR or above Q3 + 1.5IQR
    
- [ ] D. Have zero variance
    

What does Normalization (Min-Max Scaling) do?

- [ ] A. Converts text data into numeric form
    
- [ ] B. Rescales features between 0 and 1
    
- [ ] C. Removes missing values
    
- [ ] D. Detects correlation
    

What is one key advantage of data preprocessing?

- [ ] A. Guarantees perfect model accuracy
    
- [ ] B. Eliminates need for EDA
    
- [ ] C. Removes all features
    
- [ ] D. Reduces overfitting
