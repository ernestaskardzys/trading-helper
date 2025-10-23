import unittest

import pandas as pd
import numpy as np

from trading_helper.volatility.volatility import calculate_daily_volatility, calculate_monthly_volatility, calculate_yearly_volatility, expected_move_of_stock_based_on_iv, implied_volatility_to_expected_move

class TestVolatility(unittest.TestCase):

    def test_implied_volatility_to_expected_move(self):
        iv = 4.17
        dte = 30

        result = implied_volatility_to_expected_move(iv, dte)

        np.testing.assert_approx_equal(result, 1.195501843)

    def test_implied_volatility_to_expected_move(self):
        iv = 4.17
        stock_price = 3.6
        dte = 30

        upper_bound_result, lower_bound_result = expected_move_of_stock_based_on_iv(iv, stock_price, dte)

        np.testing.assert_approx_equal(upper_bound_result, 11.898777798)
        np.testing.assert_approx_equal(lower_bound_result, 1.0891874963)

    def test_calculate_daily_volatility_no_column_exists(self):
        df = pd.DataFrame()

        with self.assertRaises(Exception) as context:
            calculate_daily_volatility(df, 'not_existing_column')

        self.assertTrue('Column not_existing_column is not found in DataFrame of prices!' in str(context.exception))

    def test_calculate_daily_volatility(self):
        df = pd.DataFrame({'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

        result = calculate_daily_volatility(df)

        np.testing.assert_approx_equal(result, 28.516194712972297)
    
    def test_calculate_monthly_volatility_no_column_exists(self):
        df = pd.DataFrame()

        with self.assertRaises(Exception) as context:
            calculate_monthly_volatility(df, 'not_existing_column')

        self.assertTrue('Column not_existing_column is not found in DataFrame of prices!' in str(context.exception))

    def test_calculate_monthly_volatility(self):
        df = pd.DataFrame({'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

        result = calculate_monthly_volatility(df)

        np.testing.assert_approx_equal(result, 130.67762080429506)
    
    def test_calculate_yearly_volatility_no_column_exists(self):
        df = pd.DataFrame()

        with self.assertRaises(Exception) as context:
            calculate_yearly_volatility(df, 'not_existing_column')

        self.assertTrue('Column not_existing_column is not found in DataFrame of prices!' in str(context.exception))

    def test_calculate_yearly_volatility(self):
        df = pd.DataFrame({'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

        result = calculate_yearly_volatility(df)

        np.testing.assert_approx_equal(result, 452.68055729051764)

if __name__ == '__main__':
    unittest.main()
