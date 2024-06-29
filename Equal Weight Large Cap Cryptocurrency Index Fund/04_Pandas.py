import requests
import pandas as pd

def get_top_10_cryptocurrencies():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }

    response = requests.get(url, params = params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

columns = ['Ticker', 'Price', 'Market Capitalization', 'Number of Coins to Buy']
final_dataframe = pd.DataFrame(columns = columns)

top_10_cryptos = get_top_10_cryptocurrencies()

if top_10_cryptos:
    for crypto in top_10_cryptos:
        ticker = crypto['symbol'].upper()
        price = crypto['current_price']
        market_cap = crypto['market_cap']
        new_data = pd.DataFrame([[ticker, price, market_cap, 'N/A']], columns = columns)
        final_dataframe = pd.concat([final_dataframe, new_data], ignore_index = True)
else:
    print('Failed to retrieve data.')

final_dataframe.to_csv('top_10_cryptocurrencies.csv', index=False)

print(final_dataframe)