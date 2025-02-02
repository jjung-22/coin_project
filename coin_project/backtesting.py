# 변동성 돌파전략 The Volatility Break-Out Strategy
# 변동성 돌파전략의 핵심
# 1) range 계산 : 전일 고가 - 전일 저가(하루 안에 움직인 가격의 최대 폭)
# 2) 매수기준 : 시가 기준으로 가격이 'range*k'이상 상승하면 해당 가격에 매수
# 3) k는 0.5 ~ 1 중 선택해서 사용
# 4) 매도기준 : 그 날 종가에 판매

# 업비트 일봉 데이터는 09:00 ~ 08:59:59 단위로 만들어지므로 이를 시가, 종가로 생각한다

# 백테스팅 하기
import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC") # 디폴트 = 일봉, 200개
# print(df.head())
df.to_excel("btc.xlsx")

# 해당 백테스팅은 거래수수료등을 계산하지 않았으므로 주의할 것
# 사고팔 때, 슬리피지(그 금액에 안 사질 수도 있음)가 있을 수 있으므로 감안하기..