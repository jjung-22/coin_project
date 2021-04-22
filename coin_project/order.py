import pyupbit
import pprint # 예쁘게 프린트 해줌 

# 호가정보 가져오기
# ask = 매도호가, bid = 매수호가

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)
# total_ask_size 호가 매도 총 잔량
# total_bid_size 호가 매수 총 잔량
# orderbook_units 호가
# ask_price	매도호가
# bid_price	매수호가
# ask_size	매도 잔량
# bid_size	매수 잔량

orderbook = orderbooks[0]

total_ask_size = orderbook['total_ask_size']
total_bid_size = orderbook['total_bid_size']

print("매도호가 총합 : ", total_ask_size)
print("매수호가 총합 : ", total_bid_size)