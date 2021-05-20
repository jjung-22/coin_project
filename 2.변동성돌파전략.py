import pyupbit
import time

#0.2초마다 현재가 조회

while True:
    price = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"]) #이름 추가하면 항목 늘릴 수 있음
    print(price)
    time.sleep(0.2) #0.2초마다
