import os
import pandas as pd

def load_coingecko_market_data(tickers, series_name=None, rel_path='./data'):
    market_data = {}
    lower_tickers = [ticker.lower() for ticker in tickers]

    for filename in os.listdir(rel_path):
        ticker = filename.split('-')[0].lower()

        # Load relevant data
        if ticker in lower_tickers:
            # Assume market data column order
            column_names = ['Date', 'Close Price', 'Market Cap', 'Volume']

            file_data = pd.read_csv(os.path.join(rel_path, filename))

            # Rename columns
            curr_column_names = list(file_data)
            column_names_map = {curr_column_names[i]: column_names[i] for i in range(len(column_names))}
            file_data.rename(columns=column_names_map, inplace=True)

            # Set index to date and convert to np.datetime64
            file_data.set_index(['Date'], inplace=True)
            file_data.index = pd.to_datetime(file_data.index)

            if series_name is None:
                market_data[ticker] = file_data
            else:
                market_data[ticker] = file_data[series_name]

    return market_data
