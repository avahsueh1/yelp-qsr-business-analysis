import pandas as pd
topic_df = pd.read_parquet("C:\\Users\\hsueh\\yelp-qsr-business-analysis\\data\\processed\\exploded_topics_qsr_reviews_scoped.parquet")
print(topic_df.columns)

#how many reviews per topic per brand
brand_topic_counts = (
    topic_df.groupby(["brand", "topics"])
    .size()
    .reset_index(name="review_count")
)
print(brand_topic_counts.head(5))

#how many total reviews per brand
brand_totals = (
    brand_topic_counts.groupby("brand")["review_count"]
    .sum()
    .reset_index(name = "total_reviews")
)

#brand topic rel. freq
brand_topic_share = brand_topic_counts.merge(brand_totals, how = "inner", on = "brand")
brand_topic_share["relative_freq"] = brand_topic_share["review_count"]/brand_topic_share["total_reviews"]

#creating a table easier to read
brand_topic_table_mean = (
    brand_topic_share[["brand", "topics", "relative_freq"]].pivot(
        index = "brand",
        columns = "topics",
        values = "relative_freq"
    )
    .fillna(0)
)
print(brand_topic_table_mean.head(5))
print(brand_topic_table_mean.sum(axis = 1)) #check to make sure everything adds to 1

#make another table with counts instead of means
brand_topic_table_counts = (
    brand_topic_share[["brand", "topics", "review_count"]].pivot(
        index = "brand",
        columns = "topics",
        values = "review_count"
    )
    .fillna(0).reset_index()
)

#average sentiment score in each brand
brand_topic_sent_dist = (
    topic_df.groupby(["brand", "topics"])["sentiment_score"]
    .agg(["mean", "count", "std"])
    .sort_values("brand", ascending= False)
    .reset_index()
)
brand_topic_sent_table = brand_topic_sent_dist[["brand", "topics", "mean"]].pivot(
    columns = "topics",
    values = "mean",
    index = "brand"
).fillna(0).reset_index()
print(brand_topic_sent_table.head(5))

#save to csv 
brand_topic_sent_dist.to_csv("outputs/brand_topic_sentiment_dist.csv", index = False)
brand_topic_table_mean = brand_topic_table_mean.reset_index()
brand_topic_table_mean.to_csv("outputs/brand_topic_table_mean.csv", index = False)
brand_topic_sent_table.to_csv("outputs/brand_topic_sentiment_table.csv", index = False)
brand_topic_table_counts.to_csv("outputs/brand_topic_table_counts.csv", index = False)