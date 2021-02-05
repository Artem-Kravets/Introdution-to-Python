import pandas as pd

df_amazon = pd.read_csv('data/stocks/Amazon_monthly.csv')
df_amazon["name"] = "Amazon"
final_df_amazon = df_amazon.loc[:12, :].copy()
final_df_amazon.drop(columns=["Unnamed: 0"], axis=1, inplace=True)


df_apple = pd.read_csv('data/stocks/Apple_monthly.csv')
df_apple["name"] = "Apple"
final_df_apple = df_apple.loc[:12, :].copy()
final_df_apple.drop(columns=["Unnamed: 0"], axis=1, inplace=True)

df_facebook = pd.read_csv('data/stocks/Facebook_monthly.csv')
df_facebook["name"] = "Facebook"
final_df_facebook = df_facebook.loc[:12, :].copy()
final_df_facebook.drop(columns=["Unnamed: 0"], axis=1, inplace=True)

df_microsoft = pd.read_csv('data/stocks/Microsoft_monthly.csv')
df_microsoft["name"] = "Microsoft"
final_df_microsoft = df_microsoft.loc[:12, :].copy()
final_df_microsoft.drop(columns=["Unnamed: 0"], axis=1, inplace=True)

df_netflix = pd.read_csv('data/stocks/Netflix_monthly.csv')
df_netflix["name"] = "Netflix"
final_df_netflix = df_netflix.loc[:12, :].copy()
final_df_netflix.drop(columns=["Unnamed: 0"], axis=1, inplace=True)

df_final = pd.concat([final_df_amazon, final_df_netflix, final_df_apple, final_df_microsoft, final_df_facebook])
df_final.to_csv("data/stocks/Stocks.csv")
