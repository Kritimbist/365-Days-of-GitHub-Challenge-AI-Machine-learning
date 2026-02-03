import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    "house_size": [750, 1300, 1700, 2200, 2800],
    "house_price": [80, 120, 150, 200, 250]
}

df = pd.DataFrame(data)
print(df)

plt.figure()
plt.scatter(df["house_size"], df["house_price"])
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("Before Standardization")
plt.show()

scaler = StandardScaler()
df_standardized = pd.DataFrame(
    scaler.fit_transform(df),
    columns = df.columns

)
print(df_standardized)

plt.figure()
plt.scatter(df_standardized["house_size"], df_standardized["house_price"])
plt.xlabel("Standardized House Size")
plt.ylabel("Standardized House Price")
plt.title("After Standardization")
plt.show()
