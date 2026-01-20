import pandas as pd
import numpy as np

# Create a dataset with missing values
data = {
    "Age": [20, 22, np.nan, 24, np.nan],
    "Salary": [30000, np.nan, 35000, 40000, 38000],
    "Department": ["IT", "HR", "IT", np.nan, "HR"]
}

df = pd.DataFrame(data)


print("Orginal DataFrame")
print(df)

# checking missing value
print("\nMissing value Count:")
print(df.isnull().sum())

# fill missing numerical value with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# Fill missing categorical values with mode
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
print("\nDataFrame after handling missing values:")
print(df)
