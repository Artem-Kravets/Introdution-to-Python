import concurrent.futures
import os
import time
from io import StringIO

import pandas as pd
import requests
from dotenv import load_dotenv


API_URL = 'https://www.alphavantage.co/query'
SECTOR_DATA_PATH = 'data/sector'
API_CALL_SLEEP_SEC = 60

load_dotenv()
API_KEY = os.environ.get('PERSONAL_API_KEY')


def get_sector_data(session, api_key, function):
    params = {
        'function': function,
        'apikey': api_key
    }
    print(f"Getting monthly stock data for Sector")

    response = session.get(API_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("Waiting for 1 min")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(API_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_json(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f"{SECTOR_DATA_PATH}/Sector.csv"
        ))

        print(f"Data for Sector was downloaded...")

    else:
        raise Exception(response.status_code, response.reason)


if __name__ == "__main__":

    session = requests.Session()

    if not API_KEY:
        raise Exception(
            f'Your personal API key was not set'
        )

    _args = (
        (session, API_KEY, "SECTOR")

    )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: get_sector_data(*p), _args)
