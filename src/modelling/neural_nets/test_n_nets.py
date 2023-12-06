# main.py
from rnn_model import create_rnn_model
from lstm_model import create_lstm_model
from data_preprocessing import preprocess_data

# Data preprocessing
data_url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
X_train, X_test, y_train, y_test = preprocess_data(data_url)

# Reshape data for RNN and LSTM models
X_train_rnn = X_train.values.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test_rnn = X_test.values.reshape((X_test.shape[0], X_test.shape[1], 1))

# Create RNN model
rnn_model = create_rnn_model(X_train_rnn)
rnn_model.fit(X_train_rnn, y_train, epochs=5, batch_size=64, validation_data=(X_test_rnn, y_test))

# Create LSTM model
lstm_model = create_lstm_model(X_train_rnn)
lstm_model.fit(X_train_rnn, y_train, epochs=5, batch_size=64, validation_data=(X_test_rnn, y_test))
