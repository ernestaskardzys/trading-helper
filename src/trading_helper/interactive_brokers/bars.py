from ib_async import IB, Stock, util

import pandas as pd

def get_daily_candles_for_last_year(ib: IB, stock_contract: Stock) -> pd.DataFrame:
    """
    Returns candels for last year
    """
    return get_candles(ib, stock_contract, '1 Y')

def get_candles(ib: IB, stock_contract: Stock, duration_string: str = '3 Y', bar_size: str = '1 day') -> pd.DataFrame:
    """
    Get historical candles from Interactive Brokers (IBKR)
    """
  
    bars = ib.reqHistoricalData(stock_contract, endDateTime='', durationStr=duration_string, barSizeSetting=bar_size, whatToShow='TRADES', useRTH=True)
      
    df: pd.DataFrame = util.df(bars)
    if df is None or df.empty:
        print(f"No bars have been found for {stock_contract.symbol}!")
        raise ValueError(f"No bars have been found for {stock_contract.symbol}!")
  
    return df