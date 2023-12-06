# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
# Assuming 'data' is your dataframe

# Feature scaling
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

# KMeans model
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_train)

# Evaluate the model
kmeans_predictions = kmeans.predict(X_test)
accuracy = accuracy_score(y_test, kmeans_predictions)
conf_matrix = confusion_matrix(y_test, kmeans_predictions)
classification_rep = classification_report(y_test, kmeans_predictions)

# Print results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{classification_rep}")
