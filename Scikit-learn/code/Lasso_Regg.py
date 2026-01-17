import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

# Datasets with noise

enigine_size = np.array([1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4])
fuel_consumption = np.array([6.5, 7.8, 6.9, 9.5, 8.2, 11.0, 9.1, 12.5])

X = enigine_size.reshape(-1,1)
y = fuel_consumption

#ols
X_b = np.c_[np.ones(len(X)), X]  # bias term
theta_ols = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

# lasso
lasso_model = Lasso(alpha=0.5)
lasso_model.fit(X,y)

#prediction
x_line = np.linspace(0.8, 2.6, 100).reshape(-1, 1)

y_ols = np.c_[np.ones(len(x_line)), x_line] @ theta_ols
y_lasso = lasso_model.predict(x_line)

#plot
plt.figure()
plt.scatter(X, y, color='black', label="Data")
plt.plot(x_line, y_ols, label="OLS", color='blue')
plt.plot(x_line, y_lasso, label="Lasso", color='red')
plt.xlabel("Engine Size (Liters)")
plt.ylabel("Fuel Consumption (L/100km)")
plt.title("OLS vs Lasso Regression")
plt.legend()
plt.show()

theta_ols, lasso_model.coef_, lasso_model.intercept_
