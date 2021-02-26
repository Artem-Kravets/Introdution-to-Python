import concurrent.futures
import os
import time
from io import StringIO

import pandas as pd
import requests
from dotenv import load_dotenv


API_URL = 'https://www.alphavantage.co/query'
STOCK_DATA_PATH = 'data/stocks'
API_CALL_SLEEP_SEC = 60

load_dotenv()
API_KEY = os.environ.get('PERSONAL_API_KEY')

STOCKS = {
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Facebook': 'FB',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Google': 'GOOGL',
    'Tencent': 'TCEHY',
    'Oracle': 'ORCL',
    'Alibaba': 'BABA',
    'Tesla': 'TSLA',
}


def get_stock_data(session, name, symbol, api_key, function, datatype):
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }
    print(f"Getting monthly stock data for {name}")

    response = session.get(API_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("Waiting for 1 min")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(API_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f"{STOCK_DATA_PATH}/{name}_monthly.csv"
        ))

        print(f"Data for {name} was downloaded...")

    else:
        raise Exception(response.status_code, response.reason)


if __name__ == "__main__":

    session = requests.Session()

    if not API_KEY:
        raise Exception(
            f'Your personal API key was not set'
        )

    _args = (
        (session, name, symbol, API_KEY, "TIME_SERIES_MONTHLY", "csv")
        for name, symbol, in STOCKS.items()
    )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: get_stock_data(*p), _args)
