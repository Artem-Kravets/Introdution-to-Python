import pandas as pd


def stocks_data_preprocessing(company_name):
    get_data = pd.read_csv(f'data/stocks/{company_name}_monthly.csv')
    df = pd.DataFrame(get_data)
    df.insert(2, "name", company_name, True)
    final_df = df.loc[:12, :].copy()
    final_df.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
    final_df.to_csv(f'data/stocks/{company_name}_monthly_after.csv')
    return final_df


def crypto_data_preprocessing(crypto_name):
    get_data = pd.read_csv(f'data/cryptos/{crypto_name}_monthly.csv')
    df = pd.DataFrame(get_data)
    df.rename(columns={'open (USD)': 'open', 'high (USD)': 'high', 'low (USD)': 'low', 'close (USD)': 'close'},
              inplace=True)
    df.insert(2, "name", crypto_name, True)
    final_df = df.loc[:12, :].copy()
    final_df.drop(columns=["Unnamed: 0", "open (USD).1", "high (USD).1", "low (USD).1", "close (USD).1",
                           "market cap (USD)"], axis=1, inplace=True)
    final_df.to_csv(f'data/cryptos/{crypto_name}_monthly_after.csv')
    return final_df


companies = ("Amazon", "Apple", "Facebook", "Microsoft", "Netflix", "Alibaba", "Tesla", "Tencent", "Oracle", "Google")
cryptos = ("Bitcoin", "Ethereum", "Ripple", "Cardano", "Binance Coin")


df_final_cryptos = pd.DataFrame()

for crypto in cryptos:
    crypto_df = crypto_data_preprocessing(crypto)
    df_final_cryptos = df_final_cryptos.append(crypto_df)

df_final_cryptos.to_csv("data/cryptos/Cryptos.csv", index=False)


df_final_stocks = pd.DataFrame()
for company in companies:
    company_df = stocks_data_preprocessing(company)
    df_final_stocks = df_final_stocks.append(company_df)

df_final_stocks.to_csv("data/stocks/Stocks.csv", index=False)
