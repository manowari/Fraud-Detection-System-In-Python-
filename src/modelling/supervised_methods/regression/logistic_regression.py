# logistic_regression.py
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def logistic_regression(X_train, X_test, y_train, y_test):
    # Implement logistic regression
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    confusion = confusion_matrix(y_test, predictions)
    report = classification_report(y_test, predictions)

    return model, accuracy, confusion, report
