# autoencoder_fraud_detection.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neural_network import MLPRegressor

# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Feature scaling
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

# Autoencoder Model
autoencoder = MLPRegressor(hidden_layer_sizes=(20, 10, 20, 10, 20), max_iter=1000, random_state=42)
autoencoder.fit(X_train, X_train)

# Reconstruction error
train_predictions = autoencoder.predict(X_train)
train_mse = np.mean(np.power(X_train - train_predictions, 2), axis=1)

threshold = np.percentile(train_mse, 99.9)  # Adjust threshold based on desired level of anomalies

# Testing
test_predictions = autoencoder.predict(X_test)
test_mse = np.mean(np.power(X_test - test_predictions, 2), axis=1)

predictions = (test_mse > threshold).astype(int)

# Evaluation
print("Autoencoder Anomaly Detection Results:")
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, predictions)}")
print(f"Classification Report:\n{classification_report(y_test, predictions)}")
