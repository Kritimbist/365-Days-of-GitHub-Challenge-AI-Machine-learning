import pandas as pd

data = {
    "employee": ["Ram", "Sita", "Hari", "Gita", "Raju"],
    "age": [23, 35, 45, 29, 60]
}
df = pd.DataFrame(data)
print(df)

def age_group(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

df["age_group"] = df["age"].apply(age_group)
print(df)
