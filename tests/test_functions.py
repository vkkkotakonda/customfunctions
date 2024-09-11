import unittest
import pandas as pd
from ffamecustomfunctions.functions import greet, yearToYearPercent, yearToYearDiff


class TestFunctions(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice")
        self.assertEqual(greet("Bob"), "Hello, Bob")

    def test_yearToYearPercent(self):
        # Prepare a sample dataframe
        data = {'Year': [2018, 2019, 2020, 2021],
                'Value': [100, 150, 200, 250]}
        df = pd.DataFrame(data)

        result_df = yearToYearPercent(df, 'Value')

        # Check the output for the YearToYearPercent column
        expected = [None, 50.0, 33.33, 25.0]
        self.assertAlmostEqual(result_df['YearToYearPercent'].iloc[1], 50.0, places=2)
        self.assertAlmostEqual(result_df['YearToYearPercent'].iloc[2], 33.33, places=2)
        self.assertAlmostEqual(result_df['YearToYearPercent'].iloc[3], 25.0, places=2)

    def test_yearToYearDiff(self):
        # Prepare a sample dataframe
        data = {'Year': [2018, 2019, 2020, 2021],
                'Value': [100, 150, 200, 250]}
        df = pd.DataFrame(data)

        result_df = yearToYearDiff(df, 'Value')

        # Check the output for the YearToYearDiff column
        expected = [None, 50, 50, 50]
        self.assertEqual(result_df['YearToYearDiff'].iloc[1], 50)
        self.assertEqual(result_df['YearToYearDiff'].iloc[2], 50)
        self.assertEqual(result_df['YearToYearDiff'].iloc[3], 50)


if __name__ == '__main__':
    unittest.main()
