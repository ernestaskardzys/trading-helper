from trading_helper.pricing.black_scholes import black_scholes

import numpy as np

import unittest


class TestBlackScholes(unittest.TestCase):

    def test_black_scholes_for_call_option(self):
        K = 100
        r = 0.1 # 10%
        T = 1 # 1 year
        sigma = 0.3 # 30%
        S = 100
        
        result = black_scholes(S, K, T, r, sigma, True)

        np.testing.assert_approx_equal(result, 16.73413358238666)

    def test_black_scholes_for_put_option(self):
        K = 100
        r = 0.1 # 10%
        T = 1 # 1 year
        sigma = 0.3 # 30%
        S = 100
        
        result = black_scholes(S, K, T, r, sigma, False)

        np.testing.assert_approx_equal(result, 7.217875385982609)
    
    def test_black_scholes_for_sofi_option(self):
        K = 30
        r = 0.0357 # 3.57%
        T = 0.00273973 # 1 day
        sigma = 1.0069 # 100.69%
        S = 27.91
        
        result = black_scholes(S, K, T, r, sigma)

        np.testing.assert_approx_equal(result, 0.0599227891998364)

if __name__ == "__main_":
    unittest.main()