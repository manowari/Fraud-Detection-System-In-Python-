# rnn_model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from data_preprocessing import preprocess_data

def create_rnn_model(X_train):
    model = Sequential()
    model.add(SimpleRNN(50, input_shape=(X_train.shape[1], 1)))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model
