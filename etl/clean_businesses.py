"""
Purpose:
Clean and normalize Yelp business data for downstream analysis.
"""
import pandas as pd
businesses = pd.read_parquet("data/raw/yelp_businesses.parquet")

#Drop missing rows in categories
businesses = businesses.dropna(subset=["categories"]) #if we can not identify them we can not confirm if they fit our criteria

#Keep relevant columns
businesses = businesses[['business_id', 'name', 'city', 'state', 'latitude', 'longitude', 'stars', 'review_count', 'categories']]

#Save cleaned data
businesses.to_parquet("data/processed/businesses_cleaned.parquet", index=False)
