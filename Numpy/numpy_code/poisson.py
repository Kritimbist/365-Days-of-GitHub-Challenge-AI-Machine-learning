import numpy as np
import matplotlib.pyplot as plt

lam = 3

data = np.random.poisson(lam=lam ,size=2000)
plt.hist(data, bins=np.arange(-0.5, max(data)+1.5, 1), edgecolor='black', density=True)
plt.title(f"Poisson Distribution (λ={lam})")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.grid(True)
plt.show()
