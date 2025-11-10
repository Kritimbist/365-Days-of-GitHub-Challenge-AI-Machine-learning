import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 1. Prepare the Data
# We create some sample data. 
# X = Independent variable (e.g., hours studied)
# y = Dependent variable (e.g., exam score)
X = np.array([1,2,3,4,5,6,7]).reshape(-1,1) # reshape(-1, 1) converts our 1D array [1, 2, 3...] into a 2D array [[1], [2], [3]...]
y = np.array([50, 58, 67, 73, 80, 85, 95])

# 2. Create and Train the Model
# Create a LinearRegression object

model = LinearRegression()

#Train the model using our data
model.fit(X,y)

# 3. View the Results (The Formula's Components)
# The model has now calculated the optimal b0 and b1
# b0 (Intercept)
intercept = model.intercept_
# b1 (Slope / Coefficient)
slope = model.coef_[0]

print(f"Intercept (b0) : {intercept}")
print(f"slope (b1) : {slope}")

print(f"formula for line is: y = {slope:.2f}x +{intercept:.2f}")

# 4. Make Predictions
# Let's predict the y values based on our X data
y_pred = model.predict(X)

# You can also predict new, unseen data
# For example, what score would someone get if they studied 8 hours?
new_X = np.array([[8]])
prediction = model.predict(new_X)
print(f"Prediction for 8 hours: {prediction[0]:.2f}")
# 5. Plot the Results
plt.scatter(X,y, color = 'blue',label='Actual data') # Plot the original data points
plt.plot(X, y_pred, color='red', label='Regression Line')  # Plot the regression line
plt.title('Simple Linear Regression')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()

