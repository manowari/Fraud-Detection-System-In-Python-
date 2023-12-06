import modelling.simple_descriptive.summary_statistics as sum_stat
import common_analysis.common_ds as cds
import pandas as pd 
import numpy as np 
import os
import utils.my_utils as util
import pandas as pd


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


def main():
    show_simple_analysis(df)

    
if __name__ == "__main__":
  main()