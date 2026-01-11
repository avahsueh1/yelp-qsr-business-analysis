## Overview
Analysis of 6M+ Yelp reviews to extract business insights
for quick-service restaurant operations, sentiment, and retention.

## Business Questions
- How does the distribution of customer attention (Share of Voice) between "Service" and "Food Quality" distinguish high-sentiment "Experience" brands from high-volume "Transaction" brands?
- How do Wait Time and Service bottlenecks drive negative reputation in major legacy brands?
- Why do market leaders with the highest review volumes (e.g., McDonald’s) frequently have consistent negative sentiment scores across all operational categories?
- Can we use specific complaints (like dirty stores or bad service) to predict when customers will quit a brand and where managers need to fix things first?

## Data
- Yelp Fusion API
- Review, business, and location metadata

## Analytical Scope
- Reviews and businesses datasets were merged on "business_id"
- Businesses that were catergorized as "restaurant"
- Only reviews with dates after 2017-01-01

## Data Extraction
Raw Yelp JSON files were initially extracted and inspected using R. 
The data was then exported to Parquet format and ingested 
into Python for cleaning, feature engineering, and analysis.

## Data Profiling
Initial inspection of the Yelp datasets revealed:
- Minimal missingness in core classification fields (e.g., categories)
- High variance in review text length, including empty and very short reviews
- Short reviews less than 6 characters were removed due to the classification of spam
- These findings informed subsequent cleaning and feature engineering steps

## Methods
- Data cleaning and feature engineering
    - Raw review data was cleaned by removing empty and spamreviews, standardizing timestamps, and removing irrelevant columns.
    - Raw business data was cleaned by removing empty reviews, standardizing timestamps, and removing irrelevant columns.
- Sentiment and topic analysis
    - Sentiment Scoring: Review text was analyzed using the VADER lexicon to assign a continuous sentiment score to each review (ranging from -1 for negative to +1 for positive).
    - Categorization: Classified reviews into discrete sentiment bins (Negative, Neutral, Positive) using a custom range [-1, -0.5, 0, 0.5, 1] to identify the intensity of customer feelings.
    - Multi-Label Topic Extraction: To handle reviews that discuss multiple subjects, reviews were "exploded" into specific operational dimensions: Cleanliness, Food Quality, Price, Service, and Wait Time.
    - Share of Voice (SOV) Modeling: Developed a normalized "Share of Voice" metric by calculating the relative frequency of each topic per brand, which provided a comparison of brand priorities regardless of their total review volume.
    - Statistical Benchmarking: Aggregated scores at the brand level to calculate the mean, count, and standard deviation. This identifies not only the highest-rated brands but also the most "volatile" brands based on respective standard deviation.
- Cohort and competitor analysis
    - Operational Benchmarking: Developed a 2D matrix of Brand vs. Topic Sentiment to identify specific operational strengths and weaknesses across different brands.


## Status
Work in progress