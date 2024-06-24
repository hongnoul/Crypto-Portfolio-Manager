import pandas as pd

final_dataframe = pd.read_csv('top_10_cryptocurrencies.csv')

writer = pd.ExcelWriter('recommended_trades.xlsx', engine = 'xlsxwriter')
final_dataframe.to_excel(writer, sheet_name='Recommended Trades', index=False)

background_color = '#0a0a23'
font_color = '#ffffff'

string_format = writer.book.add_format(
    {
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)
dollar_format = writer.book.add_format(
    {
        'num_format': '$0.00',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)
fractional_format = writer.book.add_format(
    {
        'num_format': '0.00000000',
        'font_color': font_color,
        'bg_color': background_color,
        'border': 1
    }
)

column_formats = {
    'A': ['Ticker', string_format],
    'B': ['Price', dollar_format],
    'C': ['Market Capitalization', dollar_format],
    'D': ['Number of Coins to Buy', fractional_format]
}
for column in column_formats.keys():
    writer.sheets['Recommended Trades'].set_column(f'{column}:{column}', 18, column_formats[column][1])

for column in column_formats.keys():
    writer.sheets['Recommended Trades'].write(f'{column}1', column_formats[column][0], string_format)

writer._save()