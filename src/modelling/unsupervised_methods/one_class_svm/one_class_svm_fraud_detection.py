# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
# Assuming 'data' is your dataframe

# Feature scaling
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('Class', axis=1), data['Class'], test_size=0.2, random_state=42)

# One-Class SVM model
one_class_svm = OneClassSVM(nu=0.01)
one_class_svm.fit(X_train)

# Evaluate the model
one_class_svm_predictions = one_class_svm.predict(X_test)
# One-Class SVM is an unsupervised algorithm, so it doesn't have true labels for evaluation.

# Print results
print("One-Class SVM is an unsupervised algorithm; evaluation is not applicable.")
