# lag_analysis.py

import pandas as pd

def create_lag_features(data, lag_features=['Amount'], lag_values=[1]):
    for feature in lag_features:
        for lag_value in lag_values:
            lag_column = f'{feature}_lag_{lag_value}'
            data[lag_column] = data[feature].shift(lag_value)
    
    # Drop rows with NaN values introduced by lagging
    data = data.dropna()
    
    return data

# Assuming data is preprocessed
# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Create lag features
lagged_data = create_lag_features(data)
print(lagged_data.head())
