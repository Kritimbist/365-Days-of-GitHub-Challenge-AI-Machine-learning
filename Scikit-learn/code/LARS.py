import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lars

#create synthesis datasets
np.random.seed(0)
#input
X =np.linspace(1,10,30).reshape(-1,1)

#Target variable with noise
np.random.seed(30)
y = 2.5 * X.squeeze() + np.random.randn(30)*2
# Train LARS model
lars = Lars(n_nonzero_coefs =1)
lars.fit(X,y)
#  Predictions
X_line = np.linspace(1, 10, 100).reshape(-1, 1)
y_pred = lars.predict(X_line)
#plot
plt.figure()
plt.scatter(X, y, label="Training Data")
plt.plot(X_line, y_pred, label="LARS Prediction")
plt.xlabel("Input Feature")
plt.ylabel("Target Value")
plt.title("Least Angle Regression (LARS)")
plt.legend()
plt.show()

lars.coef_, lars.intercept_
