# isolation_forest_fraud_detection.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Feature scaling
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

# Isolation Forest Model
isolation_forest = IsolationForest(contamination=0.01, random_state=42)
isolation_forest.fit(X_train)

# Predictions
predictions = isolation_forest.predict(X_test)

# Convert predictions to binary (1 for inliers, -1 for outliers)
predictions[predictions == 1] = 0
predictions[predictions == -1] = 1

# Evaluation
print("Isolation Forest Anomaly Detection Results:")
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, predictions)}")
print(f"Classification Report:\n{classification_report(y_test, predictions)}")
