# lstm_model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from data_preprocessing import preprocess_data

def create_lstm_model(X_train):
    model = Sequential()
    model.add(LSTM(50, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model
