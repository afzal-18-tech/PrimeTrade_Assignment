from src.load_data import *
from src.preprocessing import *
from src.merge_data import *
from src.config import *

trade = load_trade_data(TRADE_DATA)

sentiment = load_sentiment_data(SENTIMENT_DATA)

print(trade.head())

print(sentiment.head())

trade = clean_trade_data(trade)

sentiment = clean_sentiment_data(sentiment)

merged = merge_dataset(trade, sentiment)

merged.to_csv(MERGED_DATA, index=False)

print("Merged Dataset Saved Successfully")