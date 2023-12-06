# summary_statistics.py
import pandas as pd
import re


# ... (import necessary libraries)

def summary_statistics(data):
    # Display summary statistics
    summary_stats = data.describe()
    # ... (additional summary statistics or exploration if needed)

    return summary_stats
def print_several_random_columns(df):
    # Specify columns based on your requirements
    selected_columns = []

    # Find columns related to date or time using regular expressions
    date_time_columns = [col for col in df.columns if re.search(r'date|time', col, flags=re.IGNORECASE)]
    
    # Add the date and time columns to the selected columns list
    selected_columns.extend(date_time_columns)

    # Add 6 or fewer random columns to the selected columns list
    random_columns = list(df.columns.difference(selected_columns))[:6]
    selected_columns.extend(random_columns)

    # Print the head of the DataFrame with the selected columns
    print(df[selected_columns].head())
