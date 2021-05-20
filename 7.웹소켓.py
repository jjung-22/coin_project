import websockets
import asyncio 
import json


async def upbit_ws_client():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri) as websocket: 
        #업비트 개발문서를 참고하여 실시간 구독 신청을 위한 값을 파이썬 리스트 형태로 기술
        subscribe_fmt = [ {"ticket":"test"}, {"type": "ticker",
        "codes":["KRW-BTC"],
        "isOnlyRealtime": True
        },
        {"format":"SIMPLE"}]

        #JSON 포맷으로 변환
        subscribe_data = json.dumps(subscribe_fmt)
        #구독 신청
        await websocket.send(subscribe_data)

        #무한 루프를 통해 실시간 데이터를 전달받고 이를 화면에 출력
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)

async def main():
    await upbit_ws_client()

asyncio.run(main())