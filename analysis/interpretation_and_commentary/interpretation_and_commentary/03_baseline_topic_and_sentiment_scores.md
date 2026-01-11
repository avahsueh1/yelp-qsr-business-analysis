# Interpretation of Baseline Topic and Sentiment Scores

## Objective
- To establish industry-standard sentiment benchmarks 
across specific operational topics (Service, Wait Time, Food Quality, Cleanliness, and Price)
for future analysis of competitive gaps and strategic oppurtunities.

## Topics vs Sentiment Scores
- Highest Sentiment: Food Quality has the highest mean sentiment score of 0.724, followed closely by Price/Value.
- Lowest Sentiment: Cleanliness has the lowest baseline sentiment at 0.582, nearly 0.14 points lower than Food Quality.
- Consistency: Cleanliness has the highest standard deviation (0.6368), indicating the widest range of sentiment scores. However Food Quality has the lowest standard deviation (0.5151), indicating the most consistent sentiment across the dataset.
- Highest Volume: Service is the most discussed topic in the dataset, appearing in over 1.36 million reviews.
- Lowest Volume: Cleanliness is the least mentioned topic, with under 300k reviews, representing a significant drop in frequency compared to Service and Food Quality.

## Interpretation
- When standard deviation is this high (especially in Cleanliness at 0.63), it suggests that the customer experience is not standardized. It is likely dependent on the specific location, the time of day, or the specific staff shift. In addition, the high standard deviation consistent across categories indicates extreme bimodality.
    - Standard deviation in most categories is nearly equal to the mean, implying that the average customer experience does not actually exist. Instead, the industry is defined by volatility, where rating heavily depend on location and shift factors.