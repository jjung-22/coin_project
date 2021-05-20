import pyupbit
import numpy as np
import pandas as pd

#기존의 백테스팅 코드를 함수로 만들기
def get_hpr(ticker):
    try:
        df = pyupbit.get_ohlcv(ticker)
        df = df.loc['2021']  #2021년도에 대해서만 백테스팅

        #이동평균
        df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
        df['range'] = (df['high'] - df['low']) * 0.5
        df['target'] = df['open'] + df['range'].shift(1)
        df['bull'] = df['open'] > df['ma5']

        #수수료
        fee = 0.05
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'],df['close'] / df['target'] - fee,1)

        df['hpr'] = df['ror'].cumprod()
        df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
        return df['hpr'][-2]

    except:
        return 1

tickers = pyupbit.get_tickers() #업빗 코인의 티커 목록을 얻어옴

hprs = [] #for 루프를 실행하기 전에 리스트를 만들기
for ticker in tickers:
    hpr = get_hpr(ticker)
    hprs.append((ticker, hpr)) #리스트에 코인의 티커와 코인의 기간수익률을 저장

sorted_hprs = sorted(hprs, key=lambda x:x[1], reverse=True)  #기간수익률을 기준으로 오름차순 정렬
print(sorted_hprs[:5]) #기간수익률이 높은 5개의 코인 정보를 화면에 출력

#,encoding="UTF-8"