## Business Dataset

- Column titles consists of: ['business_id', 'name', 'address', 'city', 'state', 'postal_code',
'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'attributes', 'categories', 'hours']

- `categories`: ~0.07% of rows have missing data
  Decision: dropped rows due to negligible impact

## Reviews Dataset

- Column titles consists of: ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny',
'cool', 'text', 'date', 'text_length', 'spam']

- `text`: 0.0012159741812917365% of rows have spam reviews, 0 rows had missing reviews
  Decision: dropped spam rows due to negligible impact
