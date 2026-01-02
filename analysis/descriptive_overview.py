"""
Purpose:
Generate baseline descriptive statistics for QSR reviews
to understand rating distributions, volume trends over time, and
brand-level differences.
"""
import pandas as pd

df = pd.read_parquet("data/processed/qsr_reviews_scoped.parquet")

#Overall rating distribution of reviews["stars"]
    #stars_x = review star rating after merge
print(df["stars_x"].value_counts(normalize = True).sort_index()) #Result: 1: 13.61%, 2: 7.78%, 3: 9.60%, 4: 19.24%, 5: 49.76%

#Reviews over time
df["year"] = df["date"].dt.year
print(df["year"].value_counts(normalize = True).sort_index()) #Result: 2017: 21.59%, 2018: 23.87%, 2019: 23.77%, 201-20: 14.00%, 2021: 15.99%, 2022: 0.79%

#Review distribution based on brand
BRANDS = {
    "mcdonald": "McDonald's",
    "chick-fil-a": "Chick-fil-A",
    "taco bell": "Taco Bell",
    "wendy": "Wendy's",
    "burger king": "Burger King",
    "subway": "Subway",
    "popeyes": "Popeyes",
    "dunkin": "Dunkin'",
    "wawa": "Wawa",
    "chipotle": "Chipotle",
    "five guys": "Five Guys",
    "shake shack": "Shake Shack",
    "in-n-out": "In-N-Out",
    "in n out": "In-N-Out"
}
def assign_brands(name): 
    name = name.lower()
    for x, output in BRANDS.items():
        if x in name:
            return output
    return "Other"

df["brand"] = df["name"].apply(assign_brands)

brand_rating_dist = (
    df.groupby("brand")["stars_x"]
    .agg(["mean", "std", "count"])
    .sort_values("mean", ascending = False)
    .reset_index()                     
)
print(brand_rating_dist) #In n Out had the highest, where McDonald's has the lowest 

#Save outputs to CSV
rating_dist = df["stars_x"].value_counts(normalize = True).sort_index().reset_index()
rating_dist.to_csv("outputs/rating_distribution.csv", index=False)

year_dist = df["year"].value_counts(normalize = True).sort_index().reset_index()
year_dist.to_csv("outputs/yearly_distribution.csv", index=False)

brand_rating_dist.to_csv("outputs/brand_rating_dist.csv", index = False)

df.to_parquet("C:/Users/hsueh/yelp-qsr-business-analysis/data/processed/qsr_reviews_scoped.parquet")

