import numpy as np
import matplotlib.pyplot as plt

#Datasets
budgets = np.array([5,10,15,20,25,30,35,40])
sales = np.array([22,38,40,47,52,58,63,75])

#Add bias term
X = np.c_[np.ones(len(budgets)), budgets]
Y = sales

#OLS
theta_ols = np.linalg.inv(X.T@ X)@ X.T @ Y

# Ridge regression
lambda_val = 200
I = np.eye(X.shape[1])
I[0,0] = 0

theta_ridge = np.linalg.inv(X.T @ X + lambda_val * I) @ X.T @ Y

# prediction
x_line = np.linspace(0, 45, 100)
X_line = np.c_[np.ones(len(x_line)), x_line]

y_ols = X_line @ theta_ols
y_ridge = X_line @ theta_ridge

# plot
plt.figure()
plt.scatter(budgets, sales)
plt.plot(x_line, y_ols, label="OLS")
plt.plot(x_line, y_ridge, label="Ridge")
plt.xlabel("Advertising Budget (₹ thousands)")
plt.ylabel("Sales")
plt.title("OLS vs Ridge Regression (Advertising vs Sales)")
plt.legend()
plt.show()
