# arima_model.py
from statsmodels.tsa.statespace.sarimax import SARIMAX

def fit_ARIMA(series, order):
    model = SARIMAX(series, order=order)
    result = model.fit(disp=False)
    return result
