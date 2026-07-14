import pandas as pd

def load_trade_data(path):
    return pd.read_csv(path)

def load_sentiment_data(path):
    return pd.read_csv(path)