import requests
import pandas as pd
import sys


def get_market_data(market): # = {'KRW', 'USDT', 'BTC'}
    url = 'https://api.upbit.com/v1/market/all'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)
    data = response.json()

    df = pd.DataFrame(data)
    
    filtered_df = df[df['market'].str.startswith(market)]

    output_file = f'upbit_market_data_{market}.csv'

    filtered_df.to_csv(output_file, index=False)


def update_transaction_amount(filename):
    df = pd.read_csv(filename)

    transaction_amounts = []

    for i, market in enumerate(df['market']):
        url = f"https://api.upbit.com/v1/ticker?markets={market}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        market_data = response.json()

        if market_data and 'acc_trade_price_24h' in market_data[0]:
            transaction_amount = float(market_data[0]['acc_trade_price_24h'])
            print(transaction_amount)
        else:
            transaction_amount = 'N/A'
        
        temp_df = pd.DataFrame({'transaction amount': [transaction_amount]})
        
        if 'transaction_amounts_df' in locals():
            transaction_amounts_df = pd.concat([transaction_amounts_df, temp_df], ignore_index=True)
        else:
            transaction_amounts_df = temp_df
        
        break

    df['transaction amount'] = transaction_amounts_df['transaction amount']

    output_filename = f"updated_{filename}"
    df.to_csv(output_filename, index=False)

    print(f"Updated market data with transaction amount saved to {output_filename}")

update_transaction_amount('upbit_market_data_KRW.csv')
