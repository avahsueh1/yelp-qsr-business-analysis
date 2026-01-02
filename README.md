## Overview
Analysis of 6M+ Yelp reviews to extract business insights
for quick-service restaurant operations, sentiment, and retention.

## Business Questions
- What drives customer satisfaction and dissatisfaction?
- How do operational factors differ by location and time?
- What signals repeat visits vs churn?

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
    - Review text was analyzed using VADER and lexicon
    - A sentiment score was assigned to each review (-1 being negative and 1 being positive)
    - Classified each review as overall negative, positive, or neutral (bins = [-1, -.5, 0, .5, 1])
    - Sentiment scores were then analyzed across different brands
- Cohort and competitor analysis

## Status
Work in progress