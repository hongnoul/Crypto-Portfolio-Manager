import requests
import matplotlib.pyplot as plt

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

def visualize_cryptocurrencies(data):
    names = [crypto['name'] for crypto in data]
    market_caps = [crypto['market_cap'] for crypto in data]

    plt.figure(figsize=(10, 7))
    plt.pie(market_caps, labels=names, autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Cryptocurrencies by Market Capitalization')
    plt.axis('equal')
    plt.show()

top_10_cryptos = get_top_10_cryptocurrencies()
if top_10_cryptos:
    visualize_cryptocurrencies(top_10_cryptos)
else:
    print("Failed to retrieve data.")
