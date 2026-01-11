## yelp_business Dataset

- Column titles consists of: ['business_id', 'name', 'address', 'city', 'state', 'postal_code',
'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories', 'hours']

- `categories`: ~0.07% of rows have missing data
  Decision: dropped rows due to negligible impact

## yelp_reviews Dataset

- Column titles consists of: ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny',
'cool', 'text', 'date', 'text_length', 'spam']

- `text`: 0.0012159741812917365% of rows have spam reviews, 0 rows had missing reviews
  Decision: dropped spam rows due to negligible impact

## business_cleaned.parquet
- Column titles consists of: ['business_id', 'name', 'city', 'state', 'latitude', 'longitude',
       'stars', 'review_count', 'categories']

## reviews_cleaned.parquet
- Column titles consists of: ['review_id', 'user_id', 'business_id', 'stars', 'date', 'text']

## qsr_reviews_scoped.parquet
- Column titles consist of: ['review_id', 'user_id', 'business_id', 'stars_x', 'date', 'text',
       'name', 'city', 'state', 'latitude', 'longitude', 'stars_y',
       'review_count', 'categories', 'sentiment_score', 'sentiment_label']

## exploded_topics_qsr_reviews_scoped.parquet
- Column titles consist of: ['review_id', 'user_id', 'business_id', 'stars_x', 'date', 'text',
       'name', 'city', 'state', 'latitude', 'longitude', 'stars_y',
       'review_count', 'categories', 'sentiment_score', 'sentiment_label',
       'year', 'brand', 'topics']
- Dropped rows with na in topic

## Outputs/ brand_topic_table_mean
- A table that shows the relative frequencies of each topic in each brand (2 way table)

## Outputs/ brand_topic_table_counts
- A table that shows the amount of reviews of each topic in each brand (2 way table)

## Outputs/ brand_topic_sentiment_table
- A table that shows the average sentiment score of each topic in each brand (2 way table)

## Outputs/ brand_topic_sentiment_dist
- For each brand + topic, it shows the mean, std, and count