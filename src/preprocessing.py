import pandas as pd
import numpy as np
from scipy import stats

def identify_and_report_missing_values(df: pd.DataFrame, threshold: float = 0.05):
    """
    Identifies and reports missing values, flagging columns above a threshold.

    Args:
        df (pd.DataFrame): The input DataFrame.
        threshold (float): Percentage threshold for flagging columns.

    Returns:
        pd.Series: Missing value counts.
    """
    missing_counts = df.isna().sum()
    missing_percentage = (missing_counts / len(df)) * 100
    print("Missing Value Report:")
    display(pd.DataFrame({'Count': missing_counts, 'Percentage': missing_percentage}))
    high_null_cols = missing_percentage[missing_percentage > (threshold * 100)].index.tolist()
    if high_null_cols:
        print(f"Columns with >{threshold*100}% nulls: {', '.join(high_null_cols)}")
    return missing_counts

def impute_missing_values(df: pd.DataFrame, columns: list, strategy: str = 'median') -> pd.DataFrame:
    """
    Imputes missing values in specified columns using a given strategy.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of columns to impute.
        strategy (str): Imputation strategy ('median', 'mean', 'ffill', 'bfill').

    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns and df_copy[col].isnull().any():
            if strategy == 'median':
                df_copy[col].fillna(df_copy[col].median(), inplace=True)
            elif strategy == 'mean':
                df_copy[col].fillna(df_copy[col].mean(), inplace=True)
            elif strategy == 'ffill':
                df_copy[col].fillna(method='ffill', inplace=True)
            elif strategy == 'bfill':
                df_copy[col].fillna(method='bfill', inplace=True)
            print(f"Imputed missing values in '{col}' using '{strategy}' strategy.")
    return df_copy

def detect_and_remove_zscore_outliers(df: pd.DataFrame, num_cols: list, threshold: int = 3) -> pd.DataFrame:
    """
    Detects and removes outliers using the Z-score method.

    Args:
        df (pd.DataFrame): The input DataFrame.
        num_cols (list): List of numerical columns to check for outliers.
        threshold (int): Z-score threshold for outlier detection.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.
    """
    df_copy = df.copy()
    z = np.abs(stats.zscore(df_copy[num_cols].dropna(how='all'), nan_policy="omit"))
    z_outliers_mask = (z > threshold).any(axis=1)
    
    # Map the mask back to the original DataFrame's index
    original_indices_with_outliers = df_copy[num_cols].dropna(how='all').index[z_outliers_mask]
    
    print(f"Z-score outlier rows identified (threshold > {threshold}): {len(original_indices_with_outliers)}")
    
    df_cleaned = df_copy.drop(index=original_indices_with_outliers).reset_index(drop=True)
    print(f"Shape after removing Z-score outliers: {df_cleaned.shape}")
    return df_cleaned

def get_numeric_and_categorical_cols(df: pd.DataFrame):
    """Identifies numeric and categorical columns."""
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    # Special handling for 'Cleaning' which is int but conceptually categorical
    if 'Cleaning' in num_cols:
        num_cols.remove('Cleaning')
        if 'Cleaning' not in cat_cols:
            cat_cols.append('Cleaning')
    return num_cols, cat_cols