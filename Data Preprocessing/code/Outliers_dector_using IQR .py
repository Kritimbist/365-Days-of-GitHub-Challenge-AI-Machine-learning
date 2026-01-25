import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = np.array ([
     120, 130, 125, 128, 132, 135, 138, 140,
    145, 150, 155, 160,
    300, 320   # outliers
])
#Calculate IQR
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)
IQR = Q3 -Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Detect outliers
outliers = data[(data< lower_bound) | (data > upper_bound)]
normal_data = data[(data< lower_bound) & (data > upper_bound)]

#visualization
plt.figure()
#scatter plot
plt.scatter(normal_data,[1]* len(normal_data),label="Normal Data")
plt.scatter(outliers,[1]* len(outliers), label ="Outliers",color ="red")

#Bounds
plt.axvline(lower_bound, linestyle='--', label="Lower Bound")
plt.axvline(upper_bound, linestyle='--', label="Upper Bound")

plt.yticks()
plt.xlabel("House Price (in thousands)")
plt.title("Outlier Detection using IQR Method")
plt.legend()
plt.show()
