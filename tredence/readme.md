Tredence challenge: Time Series Forecasting

# PS:
Forecast warehouses weekly demand for next 2 months with the given 3 years of data, taking the effect of covid, seasonality and variations.

# Solution:
* Did feature engineering to extract weekday from date, product_type and is_warehouse_closed.
* separated each of the warehouse with indexes and date.
* analysed each of the ten warehouses with line plots for seasonality and trend and when they started.
* reduced the dataset (using date) for effective covide pattern and going back to normal.
* compared two features with bar charts.
* analysed effect of one feature on the other using heatmaps.
* tried dimensionality reduction with pca and visualization with tsne for classifying is_warehouse_closed.
* used chi_square test to check the effect of one categorical variable on the other.
* regression analysis using logistic and linear regression, to see the effects of multiple features on dependent variable.
* with above analysis reduced the number of features for training.
* used auto and partial correlation to decide the number of lags or size of window for previous data.
* used OHE for month and product type.
* Used LSTMs for training multivariate time series model for each of the warehouse and forecasted daily dispatch count.
* Aggregated daily disaptch counts for returning weekly dispatch count.
* Combined each warehouse back with index.
