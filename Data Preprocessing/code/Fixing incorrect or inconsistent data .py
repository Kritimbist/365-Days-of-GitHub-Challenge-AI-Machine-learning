import numpy as np
import pandas as pd

# sample data with some inconsistent and incorrect datasets
data = {
    "Age":[25,-3,30,200,28],
    "Gender": ["Male", "male", "M", "Female", " female "],
    "Salary": ["50000", "60000", "55000", "NaN", "58000"]
}
df = pd.DataFrame(data)
print("Orginal DataFrame")
print(df)

# fix inconsistent and incorrect datasets

# Replace unrealistic name with NaN
df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
# Fix inconsistent categorical values
# Standardize text format
df["Gender"] = df["Gender"].str.strip().str.lower()

# Map values to a consistent format
df["Gender"] = df["Gender"].replace(
    {
        "m":"male",
        "male": "male",
        "female":"female"
    })
# Fix incorrect data types
# Convert Salary to numeric
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
print("\nCleaned Data:")
print(df)
