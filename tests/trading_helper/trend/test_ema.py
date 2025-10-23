from trading_helper.trend.ema import calculate_ema

import pandas as pd
import numpy as np

import unittest


class TestEma(unittest.TestCase):

    def test_when_series_is_empty_return_empty(self):
        df = pd.DataFrame()

        result = calculate_ema(df)
        
        self.assertTrue(result == pd.DataFrame.empty, "Should be empty")
    
    def test_when_series_contains_values_calculate_ema(self):
        df = pd.DataFrame({'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        
        result = calculate_ema(df)
        
        np.testing.assert_approx_equal(result.iloc[-1], 6.536870912)
        np.testing.assert_approx_equal(result.iloc[-2], 5.671088640)
        np.testing.assert_approx_equal(result.iloc[-3], np.nan)
    
    def test_when_column_does_not_exist_raise_exception(self):
        not_existing_column_name = 'high'
        df = pd.DataFrame({'close': [1]})

        with self.assertRaises(ValueError) as context:
            calculate_ema(df=df, column_name=not_existing_column_name)

        self.assertTrue(f"Column '{not_existing_column_name}' does not exist in DataFrame" in str(context.exception))

if __name__ == "__main_":
    unittest.main()
