import asyncio
import websockets

async def automation_loop(websocket, path):
    i = 0
    while True:
        i += 1
        await asyncio.sleep(180)

        await websocket.send(f"Automação na iteração {i}")

start_server = websockets.serve(automation_loop, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()