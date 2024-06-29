import pandas as pd

final_dataframe = pd.read_csv('top_10_cryptocurrencies.csv')

# Input Function for Portfolio Size
def get_portfolio_size():
    portfolio_size = input('Enter the value of your portfolio: ')
    try:
        return float(portfolio_size)
    except ValueError:
        print('Please enter a number.')
        return get_portfolio_size()

portfolio_size = get_portfolio_size()

position_size = portfolio_size/final_dataframe.loc[0, 'Price']
for i in range(0, len(final_dataframe.index)):
    final_dataframe.loc[i, 'Number of Coins to Buy'] = position_size/final_dataframe.loc[i, 'Price']

final_dataframe.to_csv('top_10_cryptocurrencies.csv', index=False)

print(final_dataframe)