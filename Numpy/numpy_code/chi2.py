import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

df = 2
size = 2000

data = np.random.chisquare(df,size)
plt.hist(data, bins=30, density=True, edgecolor='black', alpha=0.7, label='Histogram')

x = np.linspace(0, max(data), 200)
pdf = chi2.pdf(x, df)
plt.plot(x, pdf, color='red', label='Theoretical PDF')

plt.title(f"Chi-Square Distribution (df={df})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
