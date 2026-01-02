"""
Purpose:
Join cleaned review and business datasets and define the
analytical scope for QSR analysis.
"""

import pandas as pd

reviews = pd.read_parquet("data/processed/reviews_cleaned.parquet")
businesses = pd.read_parquet("data/processed/businesses_cleaned.parquet")
print(reviews.columns)
print(businesses.columns)
#Join on business_id
df = reviews.merge(
    businesses,
    on="business_id",
    how="inner"
)


#Filter to restaurants only
df = df[df["categories"].str.contains("Restaurant", na=False)]


#Focus on a reasonable time window
df = df[df["date"] >= "2017-01-01"]


df.to_parquet(
    "data/processed/qsr_reviews_scoped.parquet",
    index=False
)
