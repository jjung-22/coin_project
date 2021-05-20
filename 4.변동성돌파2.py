import pyupbit
import time
import datetime

with open("upbit.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    upbit = pyupbit.Upbit(key, secret)


#목표가 계산하기, 목표가 갱신하기
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target


def buy_crypto_currency(ticker): # 잔고 조회 API를 사용해서 보유 중인 원화를 얻어옴
    krw = pyupbit.get_balance(ticker)[2]
    orderbook = pyupbit.get_orderbook(ticker)  # 호가창을 조회해서 최우선 매도 호가를 조회
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)  # 원화 잔고를 최우선 매도가로 나눠서 구매 가능한 수량을 계산
    pyupbit.buy_market_order(ticker, unit)  # 시장가 주문으로 비트코인을 매수

def sell_crypto_currency(ticker):
    unit = pyupbit.get_balance(ticker)[0]
    pyupbit.sell_market_order(ticker, unit)

def get_yesterday_ma5(ticker):   #전일의 5일 이동평균을 계산하는 get_yesterday_ma5() 함수를 정의
    df = pyupbit.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(5).mean()
    return ma[-2]


now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5('KRW-BTC')
target_price = get_target_price('KRW-BTC')  #프로그램이 시작될 때 전일의 5일 이동평균값을 계산

#매수 시도하기

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            target_price = get_target_price('KRW-BTC')
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5('KRW-BTC')   #매일 자정 5일 이동평균값을 업데이트
            sell_crypto_currency('KRW-BTC')  # 매도

        current_price = pyupbit.get_current_price('KRW-BTC')
        if (current_price > target_price) and (current_price > ma5): # 목표가뿐만 아니라 이동평균과 현재가를 비교
            buy_crypto_currency('KRW-BTC')  # 매수
    except:
        print('에러발생')
    time.sleep(1)

