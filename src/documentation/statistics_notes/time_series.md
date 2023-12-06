To flag fraudulent transactions using time series models, you can follow these general steps:

1. **Feature Engineering:**
   - Identify relevant numerical columns that might be indicative of fraudulent activity. For example, transaction amount, frequency of transactions, etc.
   - Extract relevant features from the data that could be useful for fraud detection.

2. **Model Training:**
   - Train your time series models (such as ARIMA or Exponential Smoothing) using the selected features.
   - Use historical data to fit the model and learn the normal behavior of the time series.

3. **Anomaly Detection:**
   - Use the trained model to predict the values for the test set (or future data).
   - Compare the predicted values with the actual values.
   - Identify instances where the actual values significantly deviate from the predicted values.

4. **Flagging Fraudulent Transactions:**
   - Define a threshold or criterion for flagging transactions as potentially fraudulent. This could be based on the residuals (the difference between actual and predicted values) exceeding a certain threshold.
   - Flag transactions that exceed the defined threshold as potentially fraudulent.

Here's an example implementation using the ARIMA model and residual analysis:

```python
# Assuming you have already defined functions for ARIMA modeling in arima_model.py

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from analysis_functions import analyze_time_series

# Load your DataFrame
df = pd.read_csv('your_data.csv')

# Specify column names
timestamp_column = 'timestamp'
amount_column = 'amount'

# Perform time series analysis
analyze_time_series(df, timestamp_column, amount_column, window_size=10, arima_order=(1, 1, 1))

# Get residuals from the ARIMA model
residuals = arima_result.resid

# Define a threshold for flagging transactions as potentially fraudulent
threshold = 2.0  # You may need to adjust this based on your data and analysis

# Flag transactions with residuals exceeding the threshold
df['fraud_flag'] = np.where(np.abs(residuals) > threshold, 1, 0)

# Display flagged transactions
fraudulent_transactions = df[df['fraud_flag'] == 1]
print("Fraudulent Transactions:")
print(fraudulent_transactions)
```

In this example, transactions with residuals (the difference between actual and predicted values) exceeding a certain threshold are flagged as potentially fraudulent. Adjust the threshold based on the characteristics of your data and the results of your analysis.