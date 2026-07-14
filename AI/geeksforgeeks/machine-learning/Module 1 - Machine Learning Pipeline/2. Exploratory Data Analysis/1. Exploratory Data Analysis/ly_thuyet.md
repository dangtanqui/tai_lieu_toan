Exploratory Data Analysis (EDA) is an important step in data analysis where we explore, summarize, and visualize data to understand its structure, detect patterns, identify anomalies, test assumptions, and check relationships between variables before applying any machine learning or statistical models.

![exploratory_data_analysis_eda_.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429482180/exploratory_data_analysis_eda_.webp)![exploratory_data_analysis_eda_.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429482180/exploratory_data_analysis_eda_.webp)

![exploratory_data_analysis_eda_2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260622154701023131/exploratory_data_analysis_eda_2.webp)![exploratory_data_analysis_eda_2.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260622154701023131/exploratory_data_analysis_eda_2.webp)

![recovery_and_file_organization_techniques.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429347465/recovery_and_file_organization_techniques.webp)![recovery_and_file_organization_techniques.webp](https://media.geeksforgeeks.org/wp-content/uploads/20260326110429347465/recovery_and_file_organization_techniques.webp)

Previous Pause Next 2 / 3

Importance
----------

*   Provides a clear understanding of the dataset, including the number of features, data types and data distribution.
*   Reveals patterns and relationships between different variables in the data.
*   Identifies errors and outliers that may affect analysis.
*   Highlights the most important features useful for building models.
*   Supports selecting suitable modelling techniques for better results.

Types of Exploratory Data Analysis
----------------------------------

### 1\. Univariate Analysis

[Univariate](https://www.geeksforgeeks.org/data-visualization/what-is-univariate-bivariate-multivariate-analysis-in-data-visualisation/) analysis studies one variable at a time to understand its characteristics and distribution.

*   [****Histograms****](https://www.geeksforgeeks.org/maths/histogram/)****:**** Show how data values are distributed.
*   [****Box plots****](https://www.geeksforgeeks.org/data-analysis/box-plot/)****:**** Help detect outliers and show data spread.
*   [****Bar charts****](https://www.geeksforgeeks.org/data-visualization/bar-graph-meaning-types-and-examples/)****:**** Used for categorical variables.

### ****2\. Bivariate Analysis****

[Bivariate analysis](https://www.geeksforgeeks.org/maths/bivariate-analysis/) examines the relationship between two variables to understand how they interact or influence each other. Common techniques include:

*   [****Scatter plots:****](https://www.geeksforgeeks.org/maths/scatter-plot/) Show the relationship between two numerical variables.
*   [****Correlation coefficient:****](https://www.geeksforgeeks.org/maths/pearson-correlation-coefficient/) Measures the strength of the relationship between variables .
*   [****Cross-tabulation:****](https://www.geeksforgeeks.org/data-analysis/what-is-cross-tabulation-and-how-does-it-organize-data-in-a-table/) Displays the relationship between two categorical variables.
*   [****Line graphs:****](https://www.geeksforgeeks.org/maths/line-graph/) Compare two variables over time to identify trends.
*   [****Covariance:****](https://www.geeksforgeeks.org/data-analysis/mathematics-covariance-and-correlation/) Shows how two variables change together.

### 3\. Multivariate Analysis

[Multivariate analysis](https://www.geeksforgeeks.org/r-language/multivariate-analysis-in-r/) studies three or more variables together to understand complex relationships within the dataset. Common techniques include:

*   [****Pair plots****](https://www.geeksforgeeks.org/python/pairplot-in-matplotlib/): Show relationships between multiple variables at once.
*   [****Principal Component Analysis (PCA)****](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)****:**** Reduces dimensionality while preserving important information.
*   [****Spatial analysis:****](https://www.geeksforgeeks.org/data-analysis/what-is-spatial-analysis/) Analyzes geographical patterns using maps and location-based data.

Steps for Performing Exploratory Data Analysis
----------------------------------------------

EDA involves a set of steps that help us understand the data, find patterns, detect issues and prepare the data for further analysis or modelling. It can be performed using different tools like:

*   ****Python:**** [Pandas](https://www.geeksforgeeks.org/pandas/introduction-to-pandas-in-python/) for data manipulation, [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) and [Seaborn](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) for visualizations and [Plotly](https://www.geeksforgeeks.org/python/python-plotly-tutorial/) for interactive charts.
*   ****R****: [ggplot2](https://www.geeksforgeeks.org/r-language/data-visualization-with-r-and-ggplot2/) for visualizations, [dplyr](https://www.geeksforgeeks.org/r-language/dplyr-package-in-r-programming/) for data manipulation and [tidyr](https://www.geeksforgeeks.org/r-language/tidyr-package-in-r-programming/) for organizing data.

![Steps-in-EDA](https://media.geeksforgeeks.org/wp-content/uploads/20260310144911767918/Steps-in-EDA.webp "Click to enlarge")

Common steps included in EDA

### Step 1: Understanding the Problem and the Data

The first step in any data analysis project is to fully understand the problem we're solving and the data we have. This includes asking questions like:

*   What is the goal or problem we are trying to solve?
*   What variables are present in the dataset and what do they represent?
*   What types of data are available (numerical, categorical, text etc.)?
*   Are there any data quality issues or limitations?

### Step 2: Importing and Inspecting the Data

The next step is to load the dataset into tools like [Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/) or [R](https://www.geeksforgeeks.org/r-language/r-programming-for-data-science/) and inspect it. These checks give a basic understanding of the dataset.

*   Load the dataset properly.
*   Check the number of rows and columns.
*   Identify missing values.
*   Verify the data type of each variable.
*   Look for errors, invalid values or unusual data points.

### Step 3: Handling Missing Data

[Missing data](https://www.geeksforgeeks.org/data-analysis/handling-missing-values-machine-learning/) is common in many datasets and can affect the quality of analysis. During EDA, it is important to identify and handle missing values properly to avoid incorrect results.

*   Understand why data is missing, as this helps in selecting the right approach.
*   Decide whether to remove or fill missing values, since removal can cause bias while imputation preserves data.
*   Use suitable imputation methods such as mean, median, regression or machine learning techniques like [KNN](https://www.geeksforgeeks.org/machine-learning/how-knn-imputer-works-in-machine-learning/) or [decision trees](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/).
*   Consider the impact of missing data, as it can still introduce uncertainty even after imputation.

### Step 4: Exploring Data Characteristics

After handling missing data, the next step is to examine the main characteristics of the dataset. This helps us understand how the data is distributed, detect unusual values and identify potential issues before further analysis.

*   Check [data distribution](https://www.geeksforgeeks.org/data-science/exploring-data-distribution-set-1/) to understand how values are spread across the dataset.
*   Measure [central tendency](https://www.geeksforgeeks.org/data-science/central-tendency/) using mean, median and mode to find the typical value of the data.
*   Measure variability using [standard deviation](https://www.geeksforgeeks.org/maths/standard-deviation-formula/) to see how much the values vary.
*   Analyze distribution shape using [skewness and kurtosis.](https://www.geeksforgeeks.org/data-science/difference-between-skewness-and-kurtosis/)
*   Identify outliers or anomalies that may affect the analysis.

### Step 5: Performing Data Transformation

Data transformation prepares the dataset for better analysis and modelling. Depending on the dataset, we may need to modify or convert the data so that it is in a suitable format for analysis.

*   Scaling or normalizing numerical variables like [min-max scaling](https://www.geeksforgeeks.org/machine-learning/standardscaler-minmaxscaler-and-robustscaler-techniques-ml/) or [standardization](https://www.geeksforgeeks.org/machine-learning/what-is-standardization-in-machine-learning/).
*   Encoding categorical variables for machine learning like [one-hot encoding](https://www.geeksforgeeks.org/machine-learning/ml-one-hot-encoding/) or [label encoding.](https://www.geeksforgeeks.org/machine-learning/ml-label-encoding-of-datasets-in-python/)
*   Applying mathematical transformations like [logarithmic square root](https://www.geeksforgeeks.org/dsa/square-root-number-using-log/) to correct skewness or non linearity.
*   [Creating new features](https://www.geeksforgeeks.org/machine-learning/feature-selection-techniques-in-machine-learning/) by deriving useful information from existing variables
*   Aggregating or grouping data based on specific variables or conditions.

### Step 6: Visualizing Relationship of Data

[Data visualization](https://www.geeksforgeeks.org/data-visualization/data-visualization-and-its-importance/) helps us understand patterns, trend and relationships in the dataset that may not be clear from numbers alone.

*   Bar charts and pie charts help analyze categorical data distribution.
*   Histograms, box plots and density plots show distribution and detect outliers in numerical data.
*   Scatter plots and correlation measures help analyze relationships between variables.

### Step 7: Handling Outliers

[Outliers](https://www.geeksforgeeks.org/machine-learning/machine-learning-outlier/) are data points that differ significantly from other observations. They may arise due to errors or genuine variations in the data.

*   Using statistical methods such as [Interquartile Range (IQR)](https://www.geeksforgeeks.org/maths/interquartile-range/) or [Z-score](https://www.geeksforgeeks.org/data-science/z-score-in-statistics/) to identify extreme values.
*   Analyze outliers carefully before taking any action.
*   Use domain knowledge to determine whether they are valid or erroneous.
*   Apply techniques like capping or transformation if necessary.
*   Remove outliers only when they are clearly incorrect or harmful to analysis.

### Step 8: Communicate Findings and Insights

The final step in EDA is to clearly present the results of the analysis. This helps others understand the insights discovered and the conclusions drawn from the data.

*   State the goal and scope of the analysis.
*   Provide background or context so the approach is easy to understand.
*   Use visualizations to support findings and make results clearer.
*   Highlight key insights, patterns, or anomalies discovered in the data.
*   Mention limitations or challenges faced during the analysis.
*   Suggest next steps or areas that require further investigation.

Application
-----------

*   Market analysis and customer segmentation
*   Risk assessment in finance and insurance
*   Quality control in manufacturing
*   Healthcare data analysis and disease prediction
*   Recommendation systems and product optimization

Suggested Quiz
----------

Which of the following is NOT a key benefit of performing Exploratory Data Analysis (EDA)?

*   A
    
    Identifying data errors and outliers
    
*   B
    
    Selecting important features for modeling
    
*   C
    
    Automatically building predictive models
    
*   D
    
    Understanding data distribution and patterns
    

Which type of EDA focuses on analyzing the relationship between two variables?

*   A
    
    Univariate Analysis
    
*   B
    
    Bivariate Analysis
    
*   C
    
    Multivariate Analysis
    
*   D
    
    Time Series Analysis
    

When handling missing data during EDA, which method involves filling missing values with the mean or median?

*   A
    
    Deletion
    
*   B
    
    Imputation
    
*   C
    
    Normalization
    
*   D
    
    Transformation
    

Which method is commonly used to detect outliers in numerical data?

*   A
    
    Interquartile Range (IQR)
    
*   B
    
    Cross-tabulation
    
*   C
    
    One-hot Encoding
    
*   D
    
    Correlation Matrix
    

You discover a highly skewed numerical column. Which transformation is often used to reduce skewness for EDA or modeling?

*   A
    
    Squaring the values
    
*   B
    
    Taking the logarithm of the values
    
*   C
    
    Replacing values with NaN
    
*   D
    
    Converting to string
