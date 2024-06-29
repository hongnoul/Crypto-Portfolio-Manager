import requests

def daily_momentum(ticker):
    url = 'https://api.upbit.com/v1/candles/days'
    headers = {'accept': 'application/json'}
    params = {
        'market': f'KRW-{ticker}',
        'count': '1',
        'convertingPriceUnit': 'KRW'
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            change_rate = data[0]['change_rate']
            return change_rate * 100
        else:
            return 'No data available'
    else:
        return f'Error: {response.status_code}'

# Example Usage
#
# ticker = 'ETH'
#
# print(daily_momentum(ticker))
