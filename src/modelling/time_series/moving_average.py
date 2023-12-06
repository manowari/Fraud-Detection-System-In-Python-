# moving_average.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url)
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

# Calculate the rolling mean (moving average)
window_size = 12
rolling_mean = data['Passengers'].rolling(window=window_size).mean()

# Plot the original time series and the moving average
plt.figure(figsize=(10, 6))
plt.plot(data['Passengers'], label='Original Time Series')
plt.plot(rolling_mean, label=f'Moving Average (window={window_size})', color='orange')
plt.title('Time Series with Moving Average')
plt.xlabel('Year')
plt.ylabel('Passenger Count')
plt.legend()
plt.show()
