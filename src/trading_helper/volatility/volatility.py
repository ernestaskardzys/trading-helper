from math import exp, sqrt
import pandas as pd

DAYS_IN_YEAR = 365
NUMBER_OF_TRADING_DAYS_IN_MONTH = 21
NUMBER_OF_TRADING_DAYS_IN_YEAR = 252

def implied_volatility_to_expected_move(implied_volatility: float, dte: int) -> float:
    """
    Calculate Expected Move from Implied Volatility (IV). Uses Square Root of Time rule, where:

    Expected Move = IV x sqrt(Days to Expiration / 365)

    For example:
    implied_volatility - 4.17 (i.e. 417%)
    dte - 30
    """
    return implied_volatility * sqrt(dte / DAYS_IN_YEAR)

def expected_move_of_stock_based_on_iv(implied_volatility: float, stock_price: float, dte: int, standard_deviations: int = 1) -> tuple[float, float]:
    """
    Calculate Expected Move of stock, based on implied volatility (IV). Returns results within standard deviations.

    Uses formula:
    Expected Move = standard_deviations x stock_price x e^(+/- IV to Expected Move)

    For example:
    implied_volatility - 4.17 (i.e. 417%)
    stock_price - 3.6
    dte - 30
    """
    expected_move_from_implied_volatility = implied_volatility_to_expected_move(implied_volatility, dte)

    expected_move_of_stock_upper_bound = standard_deviations * stock_price * exp(expected_move_from_implied_volatility)
    expected_move_of_stock_lower_bound = standard_deviations * stock_price * exp((-1) * expected_move_from_implied_volatility)

    return expected_move_of_stock_upper_bound, expected_move_of_stock_lower_bound

def calculate_daily_volatility(df: pd.DataFrame, price_column: str = 'close') -> float:
    """
    Calculates daily volatility in percentages from closing prices
    """
    if price_column not in df.columns:
        raise ValueError(f"Column {price_column} is not found in DataFrame of prices!")
    
    returns = 100 * df[price_column].pct_change().dropna()

    return returns.std()

def calculate_monthly_volatility(df: pd.DataFrame, price_column: str = 'close') -> float:
    """
    Calculates monthly volatility in percentages from closing prices.

    Returns monthly volatility as percentage
    """
    if price_column not in df.columns:
        raise ValueError(f"Column {price_column} is not found in DataFrame of prices!")
    
    daily_volatility = calculate_daily_volatility(df, price_column)
    return daily_volatility * sqrt(NUMBER_OF_TRADING_DAYS_IN_MONTH)

def calculate_yearly_volatility(df: pd.DataFrame, price_column: str = 'close') -> float:
    """
    Calculates yearly volatility in percentages from closing prices.

    Returns yearly volatility as percentage
    """
    if price_column not in df.columns:
        raise ValueError(f"Column {price_column} is not found in DataFrame of prices!")
    
    daily_volatility = calculate_daily_volatility(df, price_column)

    return daily_volatility * sqrt(NUMBER_OF_TRADING_DAYS_IN_YEAR)