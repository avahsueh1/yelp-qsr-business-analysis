"""
Purpose:
Use quantified review text to determine customer sentiment scores across brands.
"""

import pandas as pd
df = pd.read_parquet("data/processed/qsr_reviews_scoped.parquet")

#sentiment across brands
brand_sent_dist = (
    df.groupby("brand")["sentiment_score"]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending=False)
)
print(brand_sent_dist)

brand_sent_dist.to_csv("outputs/brand_sent_dist.csv")