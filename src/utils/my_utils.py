import os
import pandas as pd

def split_csv_and_retain_first_half(input_file, output_file_first_half):
    """
    Split a CSV file into two halves and retain the first half with headers.

    Parameters:
    - input_file: str, the path to the input CSV file.
    - output_file_first_half: str, the path to save the first half with headers.
    """

    # Load the entire CSV file
    df = pd.read_csv(input_file)

    # Get the number of rows in the DataFrame
    num_rows = len(df)

    # Calculate the midpoint to split the data
    midpoint = num_rows // 2

    # Retain the first half with headers
    first_half = df.iloc[:midpoint]

    # Save the first half to a new CSV file
    first_half.to_csv(output_file_first_half, index=False)

    print(f"First half with headers saved to '{output_file_first_half}'")


def delete_files_by_name(root_dir, file_name):
    '''
 deletes certain files in a tree    
# Specify the root directory and file name to delete
root_directory = os.getcwd()
file_to_delete = "__init__.py"

# Call the function to delete files with the specified name
delete_files_by_name(root_directory, file_to_delete)

    '''
    
    
    for foldername, subfolders, filenames in os.walk(root_dir):
        file_path = os.path.join(foldername, file_name)

        # Check if the file with the specified name exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_name} in {foldername}")



def normalize_windows_path(path):
    normalized_path = os.path.normpath(path)
    return normalized_path
