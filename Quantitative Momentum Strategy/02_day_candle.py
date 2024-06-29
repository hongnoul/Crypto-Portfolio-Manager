# Documentation: https://docs.upbit.com/reference/%EC%9D%BCday-%EC%BA%94%EB%93%A4-1

import requests

url = 'https://api.upbit.com/v1/candles/days'

headers = {'accept': 'application/json'}

params = {
    'market': 'KRW-BTC',
    'count': '1',
    'convertingPriceUnit': 'KRW'
}

response = requests.get(url, headers=headers, params=params)

print(response.text)