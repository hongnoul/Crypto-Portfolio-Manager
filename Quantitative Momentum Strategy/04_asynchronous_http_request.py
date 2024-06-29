# Since UPbit's OpenAPI does not support batch requests, this code utilizes aiohttp to improve efficiency.

import aiohttp
import asyncio
import pandas as pd

df = pd.read_csv('top_10_cryptocurrencies.csv')
tickers = df['Ticker'].tolist()

async def fetch(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()

async def get_market_data(tickers):
    url = 'https://api.upbit.com/v1/candles/days'
    headers = {'accept': 'application/json'}
    results = {}

    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for ticker in tickers:
            params = {
                'market': f'KRW-{ticker}',
                'count': '1',
                'convertingPriceUnit': 'KRW'
            }
            tasks.append(fetch(session, url, params))
        
        responses = await asyncio.gather(*tasks)

        for ticker, response in zip(tickers, responses):
            results[ticker] = response

    return results

market_data = asyncio.run(get_market_data(tickers))

for ticker, data in market_data.items():
    print(f'{ticker}: {data}')
