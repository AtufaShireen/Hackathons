PDF Format For Submission: https://docs.google.com/presentation/d/1K7A4Z18l8nzezZxmVXNzGjORxSJz5byklJX2gCr-thA/edit?usp=sharing


What we'll discuss
* Problem Statement
* EDA
* Overview and Assumptions
* Modelling

## Problem Statement
Given historical data for Implied Volatility Surface Dynamics (Moneyness,Tenor, Implied Volatility) of 2.5 years,
Forecast the volatility surface for the next 60 trading days.

## Exploratory Data Analysis
* Description
* Overview
* Correlation
* Volatilities for Different Strike Prices
* Distribution Of Volatilities Over Time
* AutoCorrelation
* Partial Correlation


### Overview
* The training dataset consists of 2.5 years of data (2017/01/05 - 2019/10/14)
* The testing dataset consists of remaining 2 months (10/15/19- 1/6/20)
* 19 different tenures (2 months to 40 years) for each date in both training and testing set.
* This can be assumed as representing an option chain for different expiration dates.

### Description
* No missing imputation required(count).
* IVs are close to each other (mean).
* Highest IV  was ~0.6872 for the tenure of 2 months for 0.1 strike price(fractioned).
* Lowest IV  was ~0.1057 for the tenure of 40 years in 1.5 strike price(fractioned).
* I.e., the higher the tenure, the lower the IV and vice versa (could be verified with scatter plots against each strike).


### Correlation, Partial Correlation, Auto Correlation
* High Correlation among IVs of strike prices
* Different strike prices follows a same pattern
* There exists skewness and kurtosis in the distribution of data, hence failure to cooperate with the lognormal distribution assumption of black scholes model.
* The relation Of Data with itself at different lagged points.
* The relation of data with its past points or  contribution of a change in that particular lag while holding others constant.
* * No constant change in trend.
* uniformity(mostly) in Residuals shows non existence of outliers and missing data.
* No seasonality change in IVs.

## Modelling
* Time Series Models
* Traditional Machine Learning Models
* LSTM

### Time series 
* The Forecasting can be performed,in a chained fashion or with multi output models. 
* An example of Such is VAR () model. 
* The model assumes the series to be stationary (This can be tested with ADF test) i.e., data will follow the similar pattern again in future.
* The cointegration test needs to be applied here, to check if two or more non stationary time series are integrated together.(This can be tested with johansen test).
* If the series are not stationary, we make it using transformations such as log transformation, log difference transformation.
* When the series has been transformed, var model using a proper lag(whichever fits best to the complete data)  can be trained using statsmodels library.

### Traditional Machine learning models
* Traditional models such as SVD, linear Regression,Decision Tree can be trained using Chained multiouput regressor.

### LSTM
* There could be multiple ways of solving Time series with LSTM:
* LSTM for Regression with Time Steps
* LSTM for Regression Using the Window Method
* LSTM with Memory Between Batches
* Stacked LSTMs with Memory Between Batches

#### Approach 1
With the Traditional machine Learning approach,
**Preprocessing:**
Changing date column to python’s dtype for time series analysis.
Changing the scale of tenure to days.
Extracting date,month,year features from date column for training model.
**Modelling:**
 DT can be used for predicting multiple outcomes.
 DT's Accuracy of Random forest is generally very high.
 DT can be used to predict multiple features.
 high correlation or VIF Score does not impact accuracy of DT.
 Data transformation or scaling can be avoided when using DT resulting in no loss of information.

**Result:**
DT resulted in 0.004 of mae on test dataset.

#### Approach 2
With the Stacked LSTMs with Memory Between Batches
**Preprocessing:**
Changing date column to python’s dtype for time series analysis.
Changing the scale of tenure to days.
Log transformation on tenure.
Adding hours time steps to add date index.

**Modelling:**
LSTM can be used for predicting multiple outcomes.
Created an architecture of 2 dense layers, with tanh activation functions.
Since the target variables are correlated, each these value is passed to next layer for prediction.
Trained for fewer epochs , 60.

**Result:**
LSTM resulted in 0.006 of mae on test dataset.


