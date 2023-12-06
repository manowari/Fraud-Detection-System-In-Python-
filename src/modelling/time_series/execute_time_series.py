# analysis_functions.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from modelling.time_series.time_series import plot_moving_average
from modelling.time_series.arima import fit_ARIMA
from modelling.time_series.exponential_smoothing import fit_exponential_smoothing

def analyze_time_series(df, timestamp_column, amount_column, window_size=10, arima_order=(1, 1, 1)):
    df[timestamp_column] = pd.to_datetime(df[timestamp_column])
    df = df.set_index(timestamp_column)
    df = df.sort_index()

    # Standardize the 'amount' column using StandardScaler
    scaler = StandardScaler()
    df['amount_scaled'] = scaler.fit_transform(df[amount_column].values.reshape(-1, 1))

    # Moving Average
    plot_moving_average(df['amount_scaled'], window_size, plot_intervals=True)

    # ARIMA
    arima_result = fit_ARIMA(df['amount_scaled'], arima_order)
    print(arima_result.summary())

    # Exponential Smoothing
    exp_smooth_result = fit_exponential_smoothing(df['amount_scaled'])
    print(exp_smooth_result.summary())
