import asyncio
import websockets
import datetime
import schedule
import time

from mlb import mlb_scrapper
from nba import nba_scrapper
from nfl import nfl_scrapper
from web_socket import handler
from yahoo_sport import soccerParser

async def send_message(message):
    async with websockets.connect("ws://your_websocket_server_address:port") as websocket:
        await websocket.send(message)

async def job():
    try:
        await send_message("Running NFL scrapper")
        nfl_scrapper()
        await send_message("NFL scrapper completed")
    except Exception as e:
        await send_message(f"An error occurred in nfl_scrapper: {e}")
    try:
        await send_message("Running MLB scrapper")
        mlb_scrapper()
        await send_message("MLB scrapper completed")
    except Exception as e:
        await send_message(f"An error occurred in mlb_scrapper: {e}")
    try:
        await send_message("Running NBA scrapper")
        nba_scrapper()
        await send_message("NBA scrapper completed")
    except Exception as e:
        await send_message(f"An error occurred in nba_scrapper: {e}")
    try:
        await send_message("Running Soccer parser")
        soccerParser()
        await send_message("Soccer parser completed")
    except Exception as e:
        await send_message(f"An error occurred in soccerParser: {e}")

async def main():
    print("Script started")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # Run forever

        print("Starting the job")
        await job()
        schedule.every(40).minutes.do(job)
        print("Job scheduled")

        while True:
            await schedule.run_pending()
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
