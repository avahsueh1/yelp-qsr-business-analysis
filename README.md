# yelp-qsr-business-analysis
## Overview
End-to-end analysis of 6M+ Yelp reviews to extract business insights for quick-service restaurant operations, sentiment, and retention.

## Business Questions
- What drives customer satisfaction and dissatisfaction?
- How do operational factors differ by location and time?
- What signals repeat visits vs churn?

## Data
- Yelp Fusion API
- Review, business, and location metadata

## Data Profiling
Initial inspection of the Yelp datasets revealed:
- Minimal to no missingness in all columns 
- High variance in review text length, including empty and very short spam-reviews

## Methods
- Data cleaning and feature engineering
    - Raw review data was cleaned by removing empty reviews, standardizing dates, and filtering out irrelevant categories
    - Raw business data was cleaned by 
- Sentiment and topic analysis
- Cohort and competitor analysis

## Data Extraction
Raw Yelp JSON files were initially extracted and inspected using R due to file compression constraints. The data was then exported to Parquet and ingested into Python for cleaning, feature engineering, and analysis.

## Status
Work in progress
