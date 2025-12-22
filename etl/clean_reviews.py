"""
Purpose:
Clean and normalize Yelp review data for downstream analysis.
"""
import pandas as pd
reviews = pd.read_parquet("data/raw/yelp_reviews.parquet")

#Drop missing or spam rows
reviews = reviews.dropna(subset=["text"])
reviews = reviews[reviews["text"].str.len() >= 6]


#Convert dates
reviews["date"] = pd.to_datetime(reviews["date"], errors ="coerce")

#Keep relevant columns
reviews = reviews[["review_id", "user_id", "business_id", "stars", "date", "text"]]

#Save cleaned data
reviews.to_parquet("data/processed/reviews_cleaned.parquet", index=False)
