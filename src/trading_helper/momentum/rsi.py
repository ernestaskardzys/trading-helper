import re
from ta.momentum import RSIIndicator

import pandas as pd

def calculate_rsi(close: pd.Series, window: int = 14) -> pd.Series:
    """
    Calculates a Relative Strength Index (RSI) for a given window
    Args:
        close(pd.Series): series with a column to calculate RSI for
        window(int): n period, default value: 14
    """
    if close.empty:
        return pd.Series.empty

    return RSIIndicator(close = close, window = window).rsi()