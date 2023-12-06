# feature_scaling.py

from sklearn.preprocessing import StandardScaler

def scale_features(data, features_to_scale=['Amount', 'Time']):
    scaler = StandardScaler()
    data[features_to_scale] = scaler.fit_transform(data[features_to_scale].values)
    
    return data

# Assuming data is preprocessed
# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Scale features
scaled_data = scale_features(data)
print(scaled_data.head())
