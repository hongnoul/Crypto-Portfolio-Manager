import requests

def get_top_10_cryptocurrencies():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

top_10_cryptos = get_top_10_cryptocurrencies()
if top_10_cryptos:
    for idx, crypto in enumerate(top_10_cryptos, start=1):
        print(f"{idx}. {crypto['name']} (Symbol: {crypto['symbol']}), Market Cap: ${crypto['market_cap']}")
else:
    print("Failed to retrieve data.")
