import pandas as pd
from ffamecustomfunctions.functions import yearToYearPercent, yearToYearDiff

# Sample DataFrame
df = pd.read_csv('d7bt_yearly.csv', parse_dates=['Period'], index_col='Period')

# Calculate year-to-year percent change
yearToYearPercent_df = yearToYearPercent(df, 'Value')

print(yearToYearPercent_df)

# Calculate year-to-year difference
yearToYearDiff_df = yearToYearDiff(df, 'Value')

print(yearToYearDiff_df)