import pyupbit
import pandas as pd

#---- 시세캔들 조회 (분봉)
# get_ohlcv(): pandas의 DataFrame으로 반환
# minute1 = 1분단위, minute3 = 3분단위, 5
min_df = pyupbit.get_ohlcv("KRW-BTC", "minute1") #최대 200개
print(min_df)

# pandas의 resample(): 1분봉 데이터프레임으로 3분봉을 만들 수 있음
min_df['open'].resample('3T').first()
min_df['high'].resample('3T').max()
min_df['low'].resample('3T').min()
min_df['close'].resample('3T').last()
min_df['volume'].resample('3T').sum()

#---- 시세캔들 조회(주봉)
week_df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week")
print(week_df)
week_df.to_csv("week_df.csv", encoding="UTF-8") #csv로 저장

#--- 시세캔들 조회(일봉)
day_df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=100)
print(day_df)

#--- 시세캔들 조회(월봉)
pd.options.display.float_format = "{:.1f}".format # float이 나오면 소수점 한자리까지만 화면에 표시해라(실제 값이 변경되는 것은 아님)
month_df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="month", count=100)
print(month_df)

