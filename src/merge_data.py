def merge_dataset(trade_df, sentiment_df):

    merged = trade_df.merge(
        sentiment_df,
        on="Date",
        how="left"
    )

    return merged