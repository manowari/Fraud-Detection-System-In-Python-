# data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    # Load the dataset
    # ...

    # Explore the data
    # ...

    return data

def preprocess_data(data):
    # Feature scaling
    scaler = StandardScaler()
    data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
    data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
