# exponential_smoothing.py
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def fit_exponential_smoothing(series, seasonal=None):
    model = ExponentialSmoothing(series, seasonal=seasonal)
    result = model.fit()
    return result
