"""
Purpose:
Initial ingestion and profiling of Yelp review and business datasets.
This script inspects schema and missing values that affect future cleaning and analysis decisions.

Outputs:
Console summaries used for documentation and ETL planning.
"""
import pandas as pd
import pyarrow.parquet as pq

# load raw yelp reviews
businesses = pd.read_parquet("data/raw/yelp_businesses.parquet")
print(f"Successfully loaded {len(businesses)} businesses.")
reviews = pd.read_parquet("data/raw/yelp_reviews.parquet")
print(f"Successfully loaded {len(reviews)} reviews.")


# Inspect schemas
print("\nBusiness columns:")
print(businesses.columns)
print("\nReview columns:")
print(reviews.columns)


#Missing data inspection
print(reviews.isna().mean().sort_values(ascending=False).head(15))
print(businesses.isna().mean().sort_values(ascending=False).head(15)) #only ~.07% of rows in 'categories' are missing


#Find and get rid of spam/empty reviews
#1) Get rid of empty reviews
missing_count = reviews["text"].isna().sum()
print(f"{missing_count} reviews are missing") #0 reviews are missing, therefore we do not have to drop any, which aligns with our previous code

#2) Get rid of spam reviews, our threshold will be <6
reviews["text_length"] = reviews["text"].astype(str).str.len()
reviews["spam"] = reviews["text_length"] < 6
print(reviews[reviews["spam"] == True]["text"].head(10))
print(reviews[reviews["spam"] == True]["text"].count()) #there are 85 spam reviews
print(f"{100*reviews["spam"].mean()}%") #0.0012159741812917365% of reviews are spam


#Date inspection
reviews["date"] = pd.to_datetime(reviews["date"], errors ="coerce")
print("\npercentage of invalid dates:", reviews["date"].isna().mean()) #percentage of invalid dates: 0.0%



