import pandas as pd

def clean_trade_data(df):

    df = df.copy()

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    df["time"] = pd.to_datetime(df["time"])

    df["Date"] = df["time"].dt.date

    return df


def clean_sentiment_data(df):

    df = df.copy()

    df.drop_duplicates(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    return df