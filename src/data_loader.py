import pandas as pd

def load_solar_data(filepath: str) -> pd.DataFrame:
    """
    Loads solar farm data from a CSV file and parses the 'Timestamp' column.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame with 'Timestamp' parsed as datetime.
    """
    try:
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return pd.DataFrame() # Return empty DataFrame on error
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def save_cleaned_data(df: pd.DataFrame, output_filepath: str):
    """
    Saves a cleaned DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_filepath (str): The path to save the CSV file.
    """
    try:
        df.to_csv(output_filepath, index=False)
        print(f"Cleaned data saved to {output_filepath}")
    except Exception as e:
        print(f"Error saving data: {e}")