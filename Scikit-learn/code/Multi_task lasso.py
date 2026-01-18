import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import MultiTaskLasso

# create synthesis datasets
np.random.seed(0)
#input features
X = np.linspace(1.0,3.0,30).reshape(-1,1)
# Multiple related targets
# Task 1: Fuel consumption
# Task 2: CO2 emission
y_fuel =3*X.squeeze()+np.random.randn(30)*0.5
y_co2 = 5 * X.squeeze() + np.random.randn(30) * 0.5

Y = np.c_[y_fuel, y_co2]  # multi-output

#multi-task lasso model

mt_lasso =MultiTaskLasso(alpha=0.5)
mt_lasso.fit(X,Y)
#prediction
X_line = np.linspace(1.0, 3.0, 100).reshape(-1, 1)
Y_pred = mt_lasso.predict(X_line)

#plot
plt.figure()
plt.scatter(X, y_fuel, label="Fuel Consumption (Data)")
plt.scatter(X, y_co2, label="CO2 Emission (Data)")
plt.plot(X_line, Y_pred[:, 0], label="Fuel Consumption (Multi-Task Lasso)")
plt.plot(X_line, Y_pred[:, 1], label="CO2 Emission (Multi-Task Lasso)")
plt.xlabel("Engine Size")
plt.ylabel("Output Value")
plt.title("Multi-Task Lasso Regression")
plt.legend()
plt.show()

mt_lasso.coef_, mt_lasso.intercept_
