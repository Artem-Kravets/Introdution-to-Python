import concurrent.futures
import os
import time
from io import StringIO

import pandas as pd
import requests
from dotenv import load_dotenv


API_URL = 'https://www.alphavantage.co/query'
CRYPTO_CURRENCIES_DATA_PATH = 'data/cryptos'
API_CALL_SLEEP_SEC = 60

load_dotenv()
API_KEY = os.environ.get('PERSONAL_API_KEY')

CRYPTO_CURRENCIES = {
    'Bitcoin': 'BTC',
    'Ethereum': 'ETH',
    'Ripple': 'XRP',
    'Cardano': 'ADA',
    'Binance Coin': 'BNB'
}


def get_crypto_currencies_data(session, name,  symbol, api_key, function, market, datatype):
    params = {
        'function': function,
        'symbol': symbol,
        'market': market,
        'apikey': api_key,
        'datatype': datatype
    }
    print(f"Getting monthly crypto currencies data for {name}")

    response = session.get(API_URL, params=params)

    if "5 calls per minute and 500 calls per day" in response.text:
        print("Waiting for 1 min")
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(API_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f"{CRYPTO_CURRENCIES_DATA_PATH}/{name}_monthly.csv"
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
        (session, name, symbol, API_KEY, "DIGITAL_CURRENCY_MONTHLY", "USD", "csv")
        for name, symbol, in CRYPTO_CURRENCIES.items()
    )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: get_crypto_currencies_data(*p), _args)
