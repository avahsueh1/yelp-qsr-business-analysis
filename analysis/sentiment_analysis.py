"""
Purpose:
Convert review text into sentiment scores and
analyze how sentiment aligns with star ratings.
"""

import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

df = pd.read_parquet("data/processed/qsr_reviews_scoped.parquet")
sia = SentimentIntensityAnalyzer()

# Compute sentiment scores
df["sentiment_score"] = df["text"].apply(
    lambda x: sia.polarity_scores(str(x))["compound"]
)

# Categorize sentiment
df["sentiment_label"] = pd.cut(
    df["sentiment_score"],
    bins=[-1, -0.05, 0.05, 1],
    labels=["negative", "neutral", "positive"]
)

# Check alignment with star ratings
sentiment_by_stars = (
    df.groupby("stars_x")["sentiment_score"]
      .mean()
      .reset_index()
)
print(sentiment_by_stars) #passed the check for accuracy

#Update data/processed/qsr_reviews_scoped.parquet by adding columns: "sentimen_label" and "sentiment_score"
df.to_parquet("data/processed/qsr_reviews_scoped.parquet")