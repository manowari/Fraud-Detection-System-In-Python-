def columns_with_full_data(df):
    '''Columns with full data'''
    
    return [column for column in df.columns if df[column].notna().all() and not (df[column] == "").any()]
def columns_without_full_data(df):
    '''Columns without full data'''
    
    result = [column for column in df.columns if df[column].isna().any() or (df[column] == "").any()]
    
    if not result:
        print("All columns have full data (no empty strings).")
    else:
        for column in result:
            print(f"Column '{column}' has at least one empty value.")
    
    return result



def remove_columns_from_df(df, columns_to_remove):
    '''Remove specified columns from the DataFrame'''
    
    df_copy = df.copy()  # Create a copy to avoid modifying the original DataFrame
    df_copy.drop(columns=columns_to_remove, inplace=True)
    
    return df_copy
