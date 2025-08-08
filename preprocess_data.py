import pandas as pd
import os

import pandas as pd

def create_features(df):
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Return'].rolling(window=5).std()
    df['Momentum'] = df['Close'] - df['Close'].shift(5)

    # Targets
    df['Target_1d'] = df['Close'].shift(-1)
    df['Target_7d'] = df['Close'].shift(-7)
    df['Target_30d'] = df['Close'].shift(-30)
    df['Target_365d'] = df['Close'].shift(-365)

    df.dropna(inplace=True)
    return df



def preprocess_all():
    input_dir = "data"
    output_dir = "processed"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")
            df = pd.read_csv(filepath, parse_dates=['Date'])
            df = create_features(df)
            df.dropna(inplace=True)
            output_path = os.path.join(output_dir, filename)
            df.to_csv(output_path, index=False)
            print(f"Saved processed data to {output_path}")

if __name__ == "__main__":
    preprocess_all()
