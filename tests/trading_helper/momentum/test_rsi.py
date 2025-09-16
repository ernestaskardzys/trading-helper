import unittest

import pandas as pd
import numpy as np

from trading_helper.momentum.rsi import calculate_rsi

class TestSum(unittest.TestCase):

    def test_when_series_is_empty_return_empty(self):
        series = pd.Series()

        result = calculate_rsi(series)

        self.assertTrue(result == pd.Series.empty, "Empty series")

    def test_calculate_rsi_for_three_days_window(self):
        series = pd.Series([4.32, 7.77, 1.33, 9.35, 6.31])

        result = calculate_rsi(series, window=3)

        np.testing.assert_approx_equal(result.iloc[-1], 51.9014849)
        np.testing.assert_approx_equal(result.iloc[-2], 68.9937409)
        np.testing.assert_approx_equal(result.iloc[-3], 26.3157894)