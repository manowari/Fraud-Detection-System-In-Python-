# feature_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def explore_data(data):
    print(data.head())
    # Add more exploratory analysis code as needed

# Load the dataset
url = "https://raw.githubusercontent.com/curiousily/Credit-Card-Fraud-Detection-using-Autoencoders-in-Keras/master/creditcard.csv"
data = pd.read_csv(url)

# Explore the data
explore_data(data)
