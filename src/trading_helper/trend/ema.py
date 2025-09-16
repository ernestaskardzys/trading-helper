import pandas as pd
from ta.trend import EMAIndicator

def calculate_ema(df: pd.DataFrame, column_name: str = 'close', window: int = 9) -> pd.DataFrame:
    """
    Calculates an Exponential Moving Average (EMA) for a given window
    Args:
        df(pd.DataFrame): DataFrame with multiple columns
        column_name(str): name of column to calculate EMA from
        window(int): n period, default value: 9
    """

    if df.empty:
        return pd.DataFrame.empty
    
    if not column_name in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in DataFrame")
    
    return EMAIndicator(df[column_name], window=window).ema_indicator()