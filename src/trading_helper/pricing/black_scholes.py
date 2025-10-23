import numpy as np

from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, call: bool = True) -> float:
    """
    Calculate option price, based on Black-Scholes formula

    Inputs:
    S - current asset price. For instance: 30
    K - strike price of the option. For instance: 50
    r - risk free rate. For instance: 0.01 - 1%
    T - time until option expiration in years. For instance: 1 - one year, 0.083 - one month and so on
    sigma - annualized volatility of the asset's returns. For instance: 0.3 - 30%
    call - true, if call option (default), false - if put option
    """
    N = norm.cdf

    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if call:
        return S * N(d1) - K * np.exp(-r*T)* N(d2)

    return K * np.exp(-r*T)*N(-d2) - S*N(-d1)     
