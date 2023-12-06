# stacking_model.py

from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_stacking_model(X_train, y_train):
    base_models = [
        ('rf_model', RandomForestClassifier()),
        ('gbm_model', GradientBoostingClassifier())
    ]
    
    stacking_model = StackingClassifier(estimators=base_models, final_estimator=LogisticRegression())
    stacking_model.fit(X_train, y_train)
    
    return stacking_model

def evaluate_stacking_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    print("Stacking Model Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, predictions)}")
    print(f"Classification Report:\n{classification_report(y_test, predictions)}")
    
    return predictions
