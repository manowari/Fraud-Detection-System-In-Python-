# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
# Assuming 'data' is your dataframe

# Feature scaling
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

# DBSCAN model
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X_train)

# Evaluate the model
dbscan_predictions = dbscan.fit_predict(X_test)
# DBSCAN is an unsupervised algorithm, so it doesn't have true labels for evaluation.

# Print results
print("DBSCAN is an unsupervised algorithm; evaluation is not applicable.")
