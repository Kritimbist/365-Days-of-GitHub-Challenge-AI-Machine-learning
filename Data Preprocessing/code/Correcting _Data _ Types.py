import pandas as pd

data = {
    "movie_id": ["101", "102", "103", "104"],          # should be numeric
    "release_year": ["2020", "2019", "2021", "2022"],  # stored as text
    "rating": ["4.5", "3.8", "4.9", "4.2"],            # numeric as string
    "is_popular": ["True", "False", "True", "False"],  # boolean as string
    "date_added": ["2021-01-10", "2020-05-20", "2022-07-15", "2021-11-01"]
}
df = pd.DataFrame(data)
print(df.dtypes)

df["movie_id"] = pd.to_numeric(df["movie_id"])
df["release_year"] = pd.to_numeric(df["release_year"])
df["rating"] = pd.to_numeric(df["rating"])

df["is_popular"] =df["is_popular"].map({"True":True,"False": False})
df["date_added"] = pd.to_datetime(df["date_added"])

print(df.dtypes)

