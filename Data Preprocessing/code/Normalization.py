import pandas as pd
from sklearn.preprocessing import  MinMaxScaler
import matplotlib.pyplot as plt

data = {
    "house_size": [800, 1200, 1500, 2000, 2500],
    "house_price": [80, 120, 150, 200, 250]
}
df = pd.DataFrame(data)
print(df)
plt.figure()
plt.scatter(df["house_size"], df["house_price"])
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("Before Normalization")
plt.show()

scalar = MinMaxScaler()
df_normalized =pd.DataFrame(
    scalar.fit_transform(df),
    columns = df.columns
)
print(df_normalized)

plt.figure()
plt.scatter(df_normalized["house_size"], df_normalized["house_price"])
plt.xlabel("Normalized House Size")
plt.ylabel("Normalized House Price")
plt.title("After Normalization")
plt.show()
