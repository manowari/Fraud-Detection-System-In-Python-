# main.py

from data_preprocessing import load_data, preprocess_data
from gbm_model import train_gbm_model, evaluate_model
from stacking_model import train_stacking_model, evaluate_stacking_model

# Load and preprocess data
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = load_data(url)
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train and evaluate GBM model
gbm_model = train_gbm_model(X_train, y_train)
gbm_predictions = evaluate_model(gbm_model, X_test, y_test)

# Train and evaluate Stacking model
stacking_model = train_stacking_model(X_train, y_train)
stacking_predictions = evaluate_stacking_model(stacking_model, X_test, y_test)
