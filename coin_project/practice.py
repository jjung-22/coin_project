## 업비트 Rest API 가져오기

import requests
# 업비트 API 참조
# https://docs.upbit.com/reference 

# ---- 마켓코드 조회
# Upbit는 마켓코드를 Rest API로 제공
# https://api.upbit.com/v1/market/all 에 접속하면 브라우저로 호출할 수 있음

mk_url="https://api.upbit.com/v1/market/all?isDetails=true" # isDetail true = 유의종목 여부 : NONE(해당없음), CAUTION(투자유의)
resp = requests.get(mk_url)
mk_data = resp.json() 

krw_tickers = []

for coin in mk_data :
    ticker = coin['market']

    if ticker.startswith("KRW"):     # 원화마켓만 가져오기
        krw_tickers.append(ticker)

print(krw_tickers)
print(len(krw_tickers))

# ---- 시세캔들 조회
# 분봉
# 1, 3, 5, 15, 10, 30, 60, 240분 단위로 받아올 수 있음
min_url="https://api.upbit.com/v1/candles/minutes/1?markets=KRW-BTC&count=100"
resp = requests.get(min_url)
min_data = resp.json() 
print(min_data)

# 주봉
week_url="https://api.upbit.com/v1/candles/weeks?count=1"
resp = requests.get(week_url)
week_data = resp.json() 
print(week_data)

# 일봉 - 링크는 기본으로 넣고 params 설정해서 가져올 수 있음
day_url="https://api.upbit.com/v1/candles/days"
params ={
    "count":"1",
    "market":"KRW-BTC"
} 
resp = requests.get(day_url, params)
day_data = resp.json() 
print("일봉", day_data)

# 월봉
month_url="https://api.upbit.com/v1/candles/months"
params ={
    "count":"1",
    "market":"KRW-BTC"
} 
resp = requests.get(month_url, params)
month_data = resp.json() 
print("월봉", month_data)

# ---- 현재가(cp) 정보 조회
cp_url="https://api.upbit.com/v1/ticker?markets=KRW-BTC"
resp = requests.get(cp_url)
cp_data = resp.json() 
print(cp_data)

# ---- 호가(order book) 정보 조회(각각 15단계로 제공) 
order_url = "https://api.upbit.com/v1/orderbook?markets=KRW-BTC"
resp = requests.get(order_url)
order_data = resp.json()
print(order_data)




