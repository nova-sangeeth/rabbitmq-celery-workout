import websockets, asyncio

async def Forward(message):
        url = 'ws://127.0.0.1:61613/'
        async with websockets.connect(url) as websocket:
                await websocket.send(message)
def xmit_Loop(message):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(Forward(message))


xmit_Loop(message='hello there')