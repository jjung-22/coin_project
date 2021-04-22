# 주문 취소
import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

# 매수주문 후 uuid 가져오기
upbit = pyupbit.Upbit(access, secret)
resp = upbit.buy_limit_order("KRW-XRP", 200, 100)
print(resp[0]['uuid'])

#주문시 리턴 받은 uuid를 사용해서 해당 주문 취소
uuid = ""
resp = upbit.cancel_order(uuid)
print(resp)