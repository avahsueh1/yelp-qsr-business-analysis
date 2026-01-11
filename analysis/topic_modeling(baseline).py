"""
Purpose:
To establish industry-standard sentiment benchmarks 
across specific operational topics (Service, Wait Time, Food Quality, Cleanliness, and Price)
for future analysis of competitive gaps and strategic oppurtunities.

"""


import pandas as pd 
import re
df = pd.read_parquet("C:/Users/hsueh/yelp-qsr-business-analysis/data/processed/qsr_reviews_scoped.parquet")
TOPICS = {
    "service": [
        "slow", "rude", "staff", "employee", "service", "cashier", "worker", 
        "manager", "attitude", "ignored", "friendly", "helpful", "crew", 
        "server", "manager", "disrespectful", "professional", "mistake", "wrong"
    ],
    "wait_time": [
        "wait", "line", "long", "minutes", "queue", "drive-thru", "drivethru", 
        "forever", "stuck", "speed", "fast", "quick", "window", "delay", "hurry"
    ],
    "food_quality": [
        "cold", "fresh", "taste", "bland", "greasy", "burnt", "soggy", "dry", 
        "old", "gross", "delicious", "hot", "flavor", "stale", "undercooked", 
        "raw", "missing", "sauce", "tasty", "warm"
    ],
    "cleanliness": [
        "dirty", "clean", "bathroom", "smell", "filthy", "tables", "floor", 
        "trash", "nasty", "sanitary", "messy", "garbage", "restroom", "toilet", 
        "sticky", "stink", "flies"
    ],
    "price_value": [
        "expensive", "cheap", "price", "value", "overpriced", "cost", "dollars", 
        "rip-off", "affordable", "worth", "portion", "size", "small", "deal", "amount"
    ]
}

# Create a topic tagging function
def tag_topics(text, topic_dict):
    text = text.lower()
    topics_found = []
    for topic, keywords in topic_dict.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", text):
                topics_found.append(topic) 
                break
    return topics_found

df["topics"] = df["text"].apply(lambda x: tag_topics(str(x), TOPICS))

#Make sure each row only has one topic
exploded_topics = df.explode("topics").dropna(subset = "topics") 
print(df[["topics", "text"]].head(10))

#Analyze topics and sentiment scores
topic_and_sentiment = (
    exploded_topics.groupby("topics")["sentiment_score"]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending = False)
    .reset_index()
)
print(topic_and_sentiment)

#Update file
exploded_topics_with_na = df.explode("topics")
exploded_topics_with_na.to_parquet("data/processed/exploded_topics_with_na_qsr_reviews_scoped.parquet",
    index=False)
exploded_topics.to_parquet("data/processed/exploded_topics_qsr_reviews_scoped.parquet", index = False)
topic_and_sentiment.to_csv("outputs/topic_and_sentiment_score_dist.csv", index = False)