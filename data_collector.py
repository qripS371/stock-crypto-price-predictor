import yfinance as yf
import pandas as pd
import os

def fetch_data(ticker, start_date="2015-01-01", end_date="2025-08-08"):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.mkdir("data")

    # ✅ Stocks
    stock_tickers = {
        "TSLA": "Tesla",
        "NVDA": "Nvidia",
        "MSFT": "Microsoft",
        "GOOGL": "Alphabet",
        "BYDDY": "BYD"  # BYD in US OTC Market
    }

    # ✅ Cryptos
    crypto_tickers = {
        "BTC-USD": "Bitcoin",
        "ETH-USD": "Ethereum",
        "SOL-USD": "Solana",
        "BNB-USD": "BinanceCoin",
        "XRP-USD": "XRP"
    }

    # ✅ Download stock data
    for ticker, name in stock_tickers.items():
        print(f"Downloading stock data for {name} ({ticker})...")
        df = fetch_data(ticker)
        df.to_csv(f"data/{ticker}.csv", index=False)
        print(f"{name} saved!")

    # ✅ Download crypto data
    for ticker, name in crypto_tickers.items():
        print(f"Downloading crypto data for {name} ({ticker})...")
        df = fetch_data(ticker)
        df.to_csv(f"data/{ticker}.csv", index=False)
        print(f"{name} saved!")
