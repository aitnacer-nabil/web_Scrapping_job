import schedule
import time

from mlb import mlb_scrapper
from nba import nba_scrapper
from nfl import nfl_scrapper
from yahoo_sport import soccerParser


def job():
    try:
        nfl_scrapper()
    except Exception as e:
        print(f"An error occurred in nfl_scrapper: {e}")
    try:
        mlb_scrapper()
    except Exception as e:
        print(f"An error occurred in mlb_scrapper: {e}")
    try:
        nba_scrapper()
    except Exception as e:
        print(f"An error occurred in nba_scrapper: {e}")
    try:
        soccerParser()
    except Exception as e:
        print(f"An error occurred in soccerParser: {e}")


job()
schedule.every(40).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

