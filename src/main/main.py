import modelling.simple_descriptive.summary_statistics as sum_stat
import common_analysis.common_ds as cds
import pandas as pd 
import numpy as np 
import os
import utils.my_utils as util
import pandas as pd

import modelling.time_series.execute_time_series as exec_ts


current_dir = os.getcwd()
my_csv_dir = util.join_paths(current_dir, 'data/raw_data_files/ccfraud2.csv' ) 
df = pd.read_csv(my_csv_dir)



def show_simple_analysis(df ):
    
    '''
    Decribe the shape of the data , 
    check for null values
    '''
    print(sum_stat.summary_statistics(df))
          
    sum_stat.print_several_random_columns(df)
    
    cds.columns_without_full_data(df)



def timeseries(df):
    timestamp_column = 'Time'
    amount_column = "Amount"
    
    exec_ts.analyze_time_series(df, timestamp_column, amount_column, window_size=10, arima_order=(1, 1, 1))




def main():
    show_simple_analysis(df)
    timeseries(df)
    
if __name__ == "__main__":
  main()
  
