Time series data is data indexed in time order, typically collected at regular intervals. It shows how things change at different points, like stock prices every day or temperature every hour.

*   It is used in industries such as finance, pharmaceuticals, social media and research.
*   Analyzing and visualizing this data helps us find trends, seasonal patterns and behaviors.
*   These insights support forecasting and guide better decision-making.
*   The main goal is to study data in time order to extract meaningful patterns and predictions.

Concepts in Time Series Analysis
--------------------------------

*   ****Trend:**** Long-term direction of data (increasing, decreasing, or stable).
*   ****Seasonality:**** Repeating patterns at regular intervals.
*   ****Moving average:**** Smooths short-term fluctuations to highlight trends.
*   ****Noise:**** Random variations without a clear pattern.
*   ****Differencing:**** Computes difference between values at a given interval.
*   ****Stationarity:**** A time series whose statistical properties (mean, variance, autocorrelation) remain constant over time.
*   ****Order:**** The order of differencing refers to the number of times the time series data needs to be differenced to achieve stationarity.
*   ****Autocorrelation****[: Autocorrelation](https://www.geeksforgeeks.org/machine-learning/autocorrelation/) is a statistical method used in time series analysis to quantify the degree of similarity between a time series and a lagged version of itself.
*   ****Resampling****: [Resampling](https://www.geeksforgeeks.org/python/how-to-resample-time-series-data-in-python/) is a technique in time series analysis that is used for changing the frequency of the data observations.

### Types of Time Series Data

Time series data is defined by time-based indexing rather than being strictly continuous or discrete. It can contain both continuous and discrete values depending on the dataset.

1.  ****Continuous Time Series****: Data recorded at regular intervals with a continuous range of values like temperature, stock prices, Sensor Data, etc.
2.  ****Discrete Time Series****: Data with distinct values or categories recorded at specific time points like counts of events, categorical statuses, etc****.****

### Visualization Approaches

1.  Use line plots or area charts for continuous data to highlight trends and fluctuations.
2.  Use bar charts or histograms for discrete data to show frequency or distribution across categories.

Practical Time Series Visualization with Python
-----------------------------------------------

Let's implement this step by step:

> We will be using the stock dataset which you can download from [here](https://media.geeksforgeeks.org/wp-content/uploads/20250122170223461909/stock_data.csv).

### Step 1: Installing and Importing Libraries

We will be using [Numpy](https://www.geeksforgeeks.org/python/numpy-tutorial/), [Pandas](https://www.geeksforgeeks.org/pandas/pandas-tutorial/), [seaborn](https://www.geeksforgeeks.org/python/introduction-to-seaborn-python/) and [Matplotlib](https://www.geeksforgeeks.org/python/python-introduction-matplotlib/) libraries.

Python`import pandas as pd import numpy as np import seaborn as sns import matplotlib.pyplot as plt from statsmodels.graphics.tsaplots import plot_acf from statsmodels.tsa.stattools import adfuller`

### Step 2: Loading the Dataset

Here we will load the dataset and use the parse\_dates parameter to convert the Date column to the DatetimeIndex format.

Python`df = pd.read_csv("/content/stock_data.csv",                   parse_dates=True,                   index_col="Date") df.head()`

****Output:****

![time1](https://media.geeksforgeeks.org/wp-content/uploads/20250517131526591586/time1.webp "Click to enlarge")

Dataset

### Step 3: Cleaning of Data

We will drop columns from the dataset that are not important for our visualization.

Python`df.drop(columns='Unnamed: 0', inplace =True) df.head()`

****Output:****

![time2](https://media.geeksforgeeks.org/wp-content/uploads/20250517131616457361/time2.webp "Click to enlarge")

Drop columns

### Step 4: Plotting High Stock Prices

Since the 'High'column is of continuous data type we will use line graph to visualize it.

*   ****sns.lineplot(data=df, x=df.index, y='High', label='High Price', color='blue')****: Plots High prices over time using the datetime index on x-axis.

Python`sns.set(style="whitegrid")   plt.figure(figsize=(12, 6)) sns.lineplot(data=df, x=df.index, y='High', label='High Price', color='blue')  plt.xlabel('Date') plt.ylabel('High') plt.title('Share Highest Price Over Time')  plt.show()`

****Output:****

![time3](https://media.geeksforgeeks.org/wp-content/uploads/20250517131703557061/time3.webp "Click to enlarge")

Line plot for Time Series data

### Step 5: Resampling Data

To better understand the trend of the data we will use the resampling method which provide a clearer view of trends and patterns when we are dealing with daily data.

*   ****df\_resampled = df.resample('ME').mean(numeric\_only=True):**** Resamples data to monthly frequency and calculates the mean of all numeric columns for each month.

Python`df_resampled = df.resample('ME').mean(numeric_only=True)   sns.set(style="whitegrid")   plt.figure(figsize=(12, 6))   sns.lineplot(data=df_resampled, x=df_resampled.index, y='High', label='Month Wise Average High Price', color='blue')  plt.xlabel('Date (Monthly)') plt.ylabel('High') plt.title('Monthly Resampling Highest Price Over Time')  plt.show()`

df\_resampled \= df.resample('ME').mean(numeric\_only\=True) 

​

sns.set(style\="whitegrid") 

​

plt.figure(figsize\=(12, 6))  

sns.lineplot(data\=df\_resampled, x\=df\_resampled.index, y\='High', label\='Month Wise Average High Price', color\='blue')

​

plt.xlabel('Date (Monthly)')

plt.ylabel('High')

plt.title('Monthly Resampling Highest Price Over Time')

​

plt.show()

****Output:****

![time4](https://media.geeksforgeeks.org/wp-content/uploads/20250517131804520255/time4.webp "Click to enlarge")

Monthly resampling

### Step 6: Detecting Seasonality with Autocorrelation

We will detect Seasonality using the autocorrelation function (ACF) plot. Peaks at regular intervals in the ACF plot suggest the presence of seasonality.

Python`if 'Date' not in df.columns:     print("'Date' is already the index or not present in the DataFrame.") else:     df.set_index('Date', inplace=True)  plt.figure(figsize=(12, 6)) plot_acf(df['High'], lags=40) plt.xlabel('Lag') plt.ylabel('Autocorrelation') plt.title('Autocorrelation Function (ACF) Plot') plt.show()`

if 'Date' not in df.columns:

    print("'Date' is already the index or not present in the DataFrame.")

else:

    df.set\_index('Date', inplace\=True)

​

plt.figure(figsize\=(12, 6))

plot\_acf(df\['High'\], lags\=40)

plt.xlabel('Lag')

plt.ylabel('Autocorrelation')

plt.title('Autocorrelation Function (ACF) Plot')

plt.show()

****Output:****

![acf_high](https://media.geeksforgeeks.org/wp-content/uploads/20250717163910301650/acf_high.webp "Click to enlarge")

Seasonality with Autocorrelation

### Step 7: Testing Stationarity with ADF test

We will perform the [ADF test](https://www.geeksforgeeks.org/python/how-to-check-if-time-series-data-is-stationary-with-python/) to formally test for stationarity.

Python`from statsmodels.tsa.stattools import adfuller  result = adfuller(df['High']) print('ADF Statistic:', result[0]) print('p-value:', result[1]) print('Critical Values:', result[4])`

from statsmodels.tsa.stattools import adfuller

​

result \= adfuller(df\['High'\])

print('ADF Statistic:', result\[0\])

print('p-value:', result\[1\])

print('Critical Values:', result\[4\])

****Output:****

![time-6](https://media.geeksforgeeks.org/wp-content/uploads/20250517132016402380/time-6.webp "Click to enlarge")

Detecting Stationarity

*   Based on the ADF Statistic we accept the null hypothesis, indicating that the data is not stationary according to the Augmented Dickey-Fuller test.
*   This suggests that differencing or other transformations may be needed to achieve stationarity before applying certain time series models.

### Step 8: Differencing to Achieve Stationarity

Differencing involves subtracting the previous observation from the current observation to remove trends or seasonality.

Python`df['high_diff'] = df['High'].diff()  plt.figure(figsize=(12, 6)) plt.plot(df['High'], label='Original High', color='blue') plt.plot(df['high_diff'], label='Differenced High', linestyle='--', color='green') plt.legend() plt.title('Original vs Differenced High') plt.show()`

df\['high\_diff'\] \= df\['High'\].diff()

​

plt.figure(figsize\=(12, 6))

plt.plot(df\['High'\], label\='Original High', color\='blue')

plt.plot(df\['high\_diff'\], label\='Differenced High', linestyle\='--', color\='green')

plt.legend()

plt.title('Original vs Differenced High')

plt.show()

****Output:****

![time7](https://media.geeksforgeeks.org/wp-content/uploads/20250517132110281933/time7.webp "Click to enlarge")

Smoothening the data

### Step 9: Smoothing Data with Moving Average

****df\['High'\].diff():**** helps in calculating the difference between consecutive values in the High column. This differencing operation is used to transform a time series into a new series that represents the changes between consecutive observations.

Python`window_size = 120 df['high_smoothed'] = df['High'].rolling(window=window_size).mean()  plt.figure(figsize=(12, 6))  plt.plot(df['High'], label='Original High', color='blue') plt.plot(df['high_smoothed'], label=f'Moving Average (Window={window_size})', linestyle='--', color='orange')  plt.xlabel('Date') plt.ylabel('High') plt.title('Original vs Moving Average') plt.legend() plt.show()`

window\_size \= 120

df\['high\_smoothed'\] \= df\['High'\].rolling(window\=window\_size).mean()

​

plt.figure(figsize\=(12, 6))

​

plt.plot(df\['High'\], label\='Original High', color\='blue')

plt.plot(df\['high\_smoothed'\], label\=f'Moving Average (Window={window\_size})', linestyle\='--', color\='orange')

​

plt.xlabel('Date')

plt.ylabel('High')

plt.title('Original vs Moving Average')

plt.legend()

plt.show()

****Output:****

![time8](https://media.geeksforgeeks.org/wp-content/uploads/20250517133642785018/time8.webp "Click to enlarge")

Original vs Moving Average

This calculates the moving average of the High column with a window size of 120(A quarter), creating a smoother curve in the ****high\_smoothed**** series. The plot compares the original High values with the smoothed version.

### Step 10: Original Data vs. Differenced Data

Printing the original and differenced data side by side we get:

Python`df_combined = pd.concat([df['High'], df['high_diff']], axis=1)  print(df_combined.head())`

df\_combined \= pd.concat(\[df\['High'\], df\['high\_diff'\]\], axis\=1)

​

print(df\_combined.head())

****Output:****

![time9](https://media.geeksforgeeks.org/wp-content/uploads/20250517133748935004/time9.PNG "Click to enlarge")

Original Data Vs Differenced Data

Hence the high\_diff column represents the differences between consecutive high values. The first value of high\_diff is NaN because there is no previous value to calculate the difference.

As there is a NaN value we will drop that proceed with our test:

Python`df.dropna(subset=['high_diff'], inplace=True) df['high_diff'].head()`

df.dropna(subset\=\['high\_diff'\], inplace\=True)

df\['high\_diff'\].head()

****Output:****

![time10](https://media.geeksforgeeks.org/wp-content/uploads/20250517133850976653/time10.PNG "Click to enlarge")

Differences between consecutive high values

After that if we conduct the ADF test:

Python`from statsmodels.tsa.stattools import adfuller  result = adfuller(df['high_diff']) print('ADF Statistic:', result[0]) print('p-value:', result[1]) print('Critical Values:', result[4])`

from statsmodels.tsa.stattools import adfuller

​

result \= adfuller(df\['high\_diff'\])

print('ADF Statistic:', result\[0\])

print('p-value:', result\[1\])

print('Critical Values:', result\[4\])

****Output:****

![time11](https://media.geeksforgeeks.org/wp-content/uploads/20250517133951917532/time11.PNG "Click to enlarge")

ADF test

Since the p-value is less than 0.05, we reject the null hypothesis and conclude that the series is stationary.

> You can download the source code from [here](https://media.geeksforgeeks.org/wp-content/uploads/20250517134209429098/Time_Series_Analysis.zip).

Suggested Quiz
----------

What does trend represent in a time series?

*   A
    
    Random noise in data
    
*   B
    
    Long-term direction of the data
    
*   C
    
    Short-term fluctuations
    
*   D
    
    Monthly seasonality
    

Which plot is commonly used to detect seasonality using autocorrelation?

*   A
    
    Histogram
    
*   B
    
    ACF plot
    
*   C
    
    Scatter plot
    
*   D
    
    Bar plot
    

What does differencing do in time series analysis?

*   A
    
    Increases noise
    
*   B
    
    Converts categorical data to numeric
    
*   C
    
    Removes trend/seasonality by subtracting previous values
    
*   D
    
    Splits data into training and testing sets
    

Which Pandas method is used to resample time series data (e.g., daily to monthly)?

*   A
    
    .shift()
    
*   B
    
    .rolling()
    
*   C
    
    .resample()
    
*   D
    
    .sort\_values()