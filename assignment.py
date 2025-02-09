import numpy as np
import pandas as pd

def create_1d_array():
    """
    Create a 1D NumPy array with values [1, 2, 3, 4, 5]
    Returns:
        numpy.ndarray: 1D array
    """
    return np.array([1,2,3,4,5])

def create_2d_array():
    """
    Create a 2D NumPy array with shape (3,3) of consecutive integers
    Returns:
        numpy.ndarray: 2D array
    """
    return np.arange(1, 10).reshape(3, 3)

def array_operations(arr):
    """
    Perform basic array operations:
    1. Calculate mean
    2. Calculate standard deviation
    3. Find max value
    Returns:
        tuple: (mean, std_dev, max_value)
    """
    mean = np.mean(arr)
    std_dev = np.std(arr)
    max_value = np.max(arr)
    return mean, std_dev, max_value

def read_csv_file(filepath):
    """
    Read a CSV file using Pandas
    Args:
        filepath (str): Path to CSV file
    Returns:
        pandas.DataFrame: Loaded dataframe
    """
    return pd.read_csv(filepath)

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame
    1. Identify number of missing values
    2. Fill missing values with appropriate method
    Returns:
        pandas.DataFrame: Cleaned dataframe
    """
    print("Number of missing values:")
    print(df.isna().sum())

    df['Age'].fillna(df['Age'].mean(), inplace=True)

    df['Salary'].fillna(df['Salary'].median(), inplace=True)

    return df

def select_data(df):
    """
    Select specific columns and rows from DataFrame
    Returns:
        pandas.DataFrame: Selected data
    """
    selected_df=df.loc[:1,['Name', 'Age','Salary']]
    return selected_df

def rename_columns(df):
    """
    Rename columns of the DataFrame
    Returns:
        pandas.DataFrame: DataFrame with renamed columns
    """
    df_renamed=df.rename(columns={'Name':'Full_name','Age':'Years','Salary':'Income'})
    return df_renamed
