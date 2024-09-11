import pandas as pd


def greet(name: str) -> str:
    """
    This function returns a greeting message.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message in the format 'Hello, {name}'.
    """
    return f"Hello, {name}"


def yearToYearPercent(df: pd.DataFrame, value_column: str) -> pd.DataFrame:
    """
    This function calculates the year-to-year percentage change for a given column in a pandas DataFrame.
    It adds a new column 'YearToYearPercent' with the percentage change between consecutive rows.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame containing time series data.
    value_column (str): The name of the column for which to calculate the percentage change.

    Returns:
    pd.DataFrame: The DataFrame with an added 'YearToYearPercent' column.
    """
    df['YearToYearPercent'] = df[value_column].pct_change() * 100
    return df


def yearToYearDiff(df: pd.DataFrame, value_column: str) -> pd.DataFrame:
    """
    This function calculates the year-to-year absolute difference for a given column in a pandas DataFrame.
    It adds a new column 'YearToYearDiff' with the difference between consecutive rows.

    Parameters:
    df (pd.DataFrame): A pandas DataFrame containing time series data.
    value_column (str): The name of the column for which to calculate the difference.

    Returns:
    pd.DataFrame: The DataFrame with an added 'YearToYearDiff' column.
    """
    df['YearToYearDiff'] = df[value_column].diff()
    return df
