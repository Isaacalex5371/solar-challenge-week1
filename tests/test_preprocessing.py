import pytest
import pandas as pd
import numpy as np
from src.preprocessing import impute_missing_values, detect_and_remove_zscore_outliers

@pytest.fixture
def sample_dataframe():
    """Fixture for a sample DataFrame with missing values and potential outliers."""
    data = {
        'col1': [1, 2, np.nan, 4, 100, 6],
        'col2': [10, np.nan, 30, 40, 50, 600],
        'col3': ['A', 'B', 'A', 'C', 'B', 'A']
    }
    return pd.DataFrame(data)

def test_impute_missing_values_median(sample_dataframe):
    df_imputed = impute_missing_values(sample_dataframe.copy(), ['col1', 'col2'], strategy='median')
    assert df_imputed['col1'].isnull().sum() == 0
    assert df_imputed['col2'].isnull().sum() == 0
    # Median of [1,2,4,6,100] is 4. Median of [10,30,40,50,600] is 40.
    assert df_imputed.loc[2, 'col1'] == 4
    assert df_imputed.loc[1, 'col2'] == 40

def test_detect_and_remove_zscore_outliers(sample_dataframe):
    # col1 has 100 as an outlier, col2 has 600 as an outlier
    num_cols = ['col1', 'col2']
    df_cleaned = detect_and_remove_zscore_outliers(sample_dataframe.copy(), num_cols, threshold=2) # Lower threshold for easier testing
    
    # Original shape: (6, 3)
    # 100 in col1 and 600 in col2 should be removed.
    # Depending on exact z-score calculation, it might remove 1 or 2 rows.
    # Let's verify that the large values are gone.
    assert not (df_cleaned['col1'] > 90).any()
    assert not (df_cleaned['col2'] > 500).any()
    assert df_cleaned.shape[0] < sample_dataframe.shape[0] # Assert some rows were removed