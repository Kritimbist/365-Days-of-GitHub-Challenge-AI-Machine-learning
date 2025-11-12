import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#  Our data (e.g., House Size vs. Price)
# np.array(...).reshape(-1, 1) is just formatting for the library

X = np.array([1400, 1600, 1700, 1800, 2000]).reshape(-1, 1) # Size (sq ft) - Adjusted to 5 samples
y = np.array([150, 200, 280, 400, 500])                   # Price (in $1000s)

# create model
model = LinearRegression()
# 3. "Train" the model
# This step automatically finds the best 'm' and 'b'
# by finding the bottom of the cost function bowl.

model.fit(X,y)

# Get the model's predictions (the 'y-hat' values)

Y_pred  = model.predict(X)

# Calculate the cost (Mean Squared Error)
# This shows us the final, lowest-possible cost (the score)
# for the best-fit line.

cost = mean_squared_error(y,Y_pred)

print(f"our data's y values(actual): {y}")
print(f"Model's y values (predicted): {Y_pred}")
print(f"Cost(MSE): {cost}")

# You can also see the 'm' and 'b' it found:

print(f"Best slope(m): {model.coef_[0]}")
print(f"Best intercept(b): {model.intercept_}")

#plotting
# Plot the actual data points
plt.scatter(X,y,color='blue',label='Actual Data(y)')
# Plot the regression line (our model's predictions)
plt.plot(X,Y_pred,color='red',linewidth=2,label='Regression line(Y_pred)')

plt.title('House Size vs Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('Price ($1000s)')
plt.legend()  #It explains what the different colors or shapes on your chart mean.
plt.grid(True) #This adds a grid (a set of faint horizontal and vertical lines) to the background of the plot.
plt.show()
