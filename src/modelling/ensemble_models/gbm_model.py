# gbm_model.py

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_gbm_model(X_train, y_train):
    gbm_model = GradientBoostingClassifier()
    gbm_model.fit(X_train, y_train)
    return gbm_model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    print("Gradient Boosting Model Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, predictions)}")
    print(f"Classification Report:\n{classification_report(y_test, predictions)}")
    
    return predictions
