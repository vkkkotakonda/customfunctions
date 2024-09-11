# FFame Custom Functions

This package provides two functions for calculating year-to-year changes in time series data:
1. `yearToYearPercent`: Calculates the year-to-year percent change.
2. `yearToYearDiff`: Calculates the year-to-year difference.

## Installation

You can install this package using pip:

```bash
pip install ffamecustomfunctions


import pandas as pd
from ffamecustomfunctions.functions import yearToYearPercent, yearToYearDiff

# Create a sample DataFrame
df = pd.read_csv('your_data.csv', parse_dates=['Date'], index_col='Date')

# Calculate year-to-year percent change
yoy_percent = yearToYearPercent(df, 'Value')

# Calculate year-to-year difference
yoy_diff = yearToYearDiff(df, 'Value')

print(yoy_percent)
print(yoy_diff)
