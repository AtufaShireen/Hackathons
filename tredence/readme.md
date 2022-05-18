Tredence challenge: Time Series Forecasting

# PS:
Forecast warehouses weekly demand for next 2 months with the given 3 years of data, taking the effect of covid, seasonality and variations.

# Solution:
* Did feature engineering to extract weekday from date, product_type and is_warehouse_closed.
* separated each of the warehouse with indexes.
* analysed each of the ten warehouses with line plots for seasonality and trend and when they started.
* compared two features with bar charts.
* analysed effect of one feature on the other using heatmaps.
* tried dimensionality reduction with tsne for classifying is_warehouse_closed.
* regression analysis using logistic and linear regression, to see the effects of multiple features on dependent variable.
* used auto and partial correlation to decide the number of lags or size of window for previous data.
* Used LSTMs for training model for each of the warehouse.
* Combined each warehouse back with index.
