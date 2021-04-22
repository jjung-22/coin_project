import pyupbit

# 원화시장 가져오기
tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)
print(len(tickers))

# BTC시장 가져오기
btc_tickers = pyupbit.get_tickers(fiat="BTC")
print(btc_tickers)
print(len(btc_tickers))

# USDT시장 가져오기
usdt_tickers = pyupbit.get_tickers(fiat="USDT")
print(usdt_tickers)
print(len(usdt_tickers))
