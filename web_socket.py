import asyncio
import websockets
import datetime

async def handler(websocket, path):
    while True:
        await asyncio.sleep(1)  # Simulate work
        now = datetime.datetime.now()
        message = f"Connection established at {now}"
        await websocket.send(message)
        print(message)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
