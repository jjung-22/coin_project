import pyupbit
def bull_market(ticker):
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]
    price = pyupbit.get_current_price(ticker)
    if price > last_ma5:
        return True
    else:
        return False


tickers = pyupbit.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, "상승장")
    else:
        print(ticker ,'하락장')
