import pandas as pd
df = pd.read_parquet("data/processed/qsr_reviews_scoped.parquet")
print(df.columns)