import pyupbit

# 현재가 정보(한 종목) 가져오기
cp_price = pyupbit.get_current_price("KRW-BTC")
print(cp_price)

# 현재가 정보(여러 종목) 가져오기
tickers=["KRW-BTC", "KRW-XRP"]  # BTC : 비트코인, XRP : 리플
price2 = pyupbit.get_current_price(tickers)
print(price2)

# 모든 원화시장 코인에 대한 현재가 정보 가져오기
krw_tickers = pyupbit.get_tickers(fiat="KRW")
prices = pyupbit.get_current_price(krw_tickers)

for k, v in prices.items() : # items() : 딕셔너리 키, 값 조회
    print(k, v)