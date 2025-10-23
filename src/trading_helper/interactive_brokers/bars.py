from ib_insync import IB, Stock, util

import pandas as pd


def get_ohlc_for_stock(ticker: str, duration_string: str = '3 Y', bar_size: str = '1 day') -> pd.DataFrame:
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=1)
    stock = Stock(ticker, 'SMART', 'USD')
    
    # Request 1 year of daily historical data
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=duration_string,
        barSizeSetting=bar_size, whatToShow='TRADES', useRTH=True
    )
    df = util.df(bars)
    ib.disconnect()
    
    if df.empty:
        raise ValueError(f"Could not stock data for {ticker}")
    
    # Set datetime as index
    df.set_index('date', inplace=True)
    df.index = pd.to_datetime(df.index)
    
    return df

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