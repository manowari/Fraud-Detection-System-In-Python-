# arima.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url)
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

# Fit ARIMA model
model = ARIMA(data['Passengers'], order=(5, 1, 2))
result = model.fit()

# Forecast future values
forecast_steps = 12
forecast = result.get_forecast(steps=forecast_steps)

# Plot the original time series and the forecast
plt.figure(figsize=(10, 6))
plt.plot(data['Passengers'], label='Original Time Series')
plt.plot(forecast.predicted_mean, label=f'ARIMA Forecast ({forecast_steps} steps ahead)', color='orange')
plt.title('ARIMA Forecasting')
plt.xlabel('Year')
plt.ylabel('Passenger Count')
plt.legend()
plt.show()
