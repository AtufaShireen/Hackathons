IIT - Guwahati : Cascade Cup

# Problem Statement - Unbalanced Classification Problem
### Rider Driver Cancellation
Given the order and rider details as described, create a model that can predict rider-driven cancellation in advance (i.e. before getting marked as cancelled or delivered)

# Assumptions & Overviews
* Classes Labels are Imbalanced, i.e., cancellation of orders id very rare instance.
* Missing percentage is almost same in train and test data.
* Both the test and train data, had more than 95% of missing values, for reassignment order,method, moreover it means cancellation of order, and hence can be dropped.
* Undelivered orders = Allotted orders-Delivered orders, hence one of these features can be dropped.

# Feature Engineering
* Date column, splitted into the following features,
  * Date
  * Weekday
  * Hour
* Created new feature from the difference of Accept time and Allot time, as time_took_accept and dropped the latter ones.
* Negative time_took_accept shows error in data collection, and were were marked as zero.
* Hours are binned into 6 categories (wrt to cancellation in training data).


# Missing Imputation
* All the null and 0 lifetime count order has cancelled orders, hence filling nans here with 0.
* Remaining columns(session_time,undelivered_orders,time_took_accept) were filled by the mean wrt rider’s history.
* Remaining Nan values in these columns were filled zero.

# Modelling
* Sampling Techniques
  * Random Up and Down Sampling with Random Forest
  * Random sampling(5218 random samples from negative class and respective positive class).
  * SMOTE
* Ensembling techniques
  * Xgboost
  * Catboost
  * LightGBM
  * Stacking
 
 # Results
* Catboost model outperformed other algorithms, in dealing with imbalanced dataset.
* Using optuna for hyper parameter tuning, the model was able to achieve ~0.64 of auc_score.

