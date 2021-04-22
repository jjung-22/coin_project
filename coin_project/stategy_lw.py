import pyupbit
import time
import datetime

# 1초에 한번씩 현재가와 현재시간 출력
# while True :
#     now = datetime.datetime.now()
#     price = pyupbit.get_current_price("KRW-BTC")
#     print(price)
#     print(now, price)
#     time.sleep(1) # API를 너무 빨리 호출하면 호출 제한이 걸리게 됨. 주의할 것


# 목표가 계산 함수
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    print(df.tail())
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

target = cal_target("KRW-BTC")
print(target)


# 목표가 갱신 (매일 아침 9시 이후 목표가 갱신 필요)
while True :
    now = datetime.datetime.now()
    #9시 0분 20초~ 30초 사이에    
    if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
        target = cal_target("KRW-BTC")
        time.sleep(10)
    
    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)
    time.sleep(1)
        
