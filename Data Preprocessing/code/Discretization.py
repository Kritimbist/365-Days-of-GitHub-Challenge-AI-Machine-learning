import pandas as pd
import matplotlib.pyplot as plt

data = {
    "age": [18, 22, 25, 30, 35, 40, 45, 50, 60, 70]
}

df = pd.DataFrame(data)
print(df)

plt.figure()
plt.plot(df["age"], marker="o")
plt.title("Before Discretization (Continuous Age Values)")
plt.ylabel("Age")
plt.show()

bins =[0,25,45,100]
labels = ["young","Adult", "Senior"]
df["age_group"] = pd.cut(df["age"], bins = bins ,labels=labels)
print(df)

df["age_group"].value_counts().plot(kind="bar")
plt.title("After Discretization (Age Groups)")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()
