import schedule
import time

from mlb import mlb_scrapper
from nba import nba_scrapper
from nfl import nfl_scrapper
from yahoo_sport import soccerParser


print("Script started")  # Add this line

def job():
    try:
        nfl_scrapper()
        print("NFL scrapper completed")
    except Exception as e:
        print(f"An error occurred in nfl_scrapper: {e}")
    try:
        mlb_scrapper()
        print("MLB scrapper completed")
    except Exception as e:
        print(f"An error occurred in mlb_scrapper: {e}")
    try:
        nba_scrapper()
        print("NBA scrapper completed")
    except Exception as e:
        print(f"An error occurred in nba_scrapper: {e}")
    try:
        soccerParser()
        print("Soccer parser completed")
    except Exception as e:
        print(f"An error occurred in soccerParser: {e}")

print("Starting the job")  # Add this line
job()
schedule.every(40).minutes.do(job)
print("Job scheduled")  # Add this line

while True:
    schedule.run_pending()
    time.sleep(1)

