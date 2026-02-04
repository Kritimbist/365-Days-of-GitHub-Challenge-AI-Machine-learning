import pandas as pd

data = {
    "day": [1, 1, 2, 2, 3, 3],
    "product": ["A", "B", "A", "B", "A", "B"],
    "sales": [100, 150, 120, 180, 130, 160]
}

df = pd.DataFrame(data)
print(df)

## Aggregate data using groupby

aggegrated = df.groupby("product")["sales"].sum()
print(aggegrated)

## Multiple Aggegration

summary = df.groupby("product")["sales"].agg(["min","max","mean"])
print(summary)
