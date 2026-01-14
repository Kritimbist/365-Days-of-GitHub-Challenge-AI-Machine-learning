import numpy as np
import matplotlib.pyplot as plt

#Datasets

hours = np.array([1,2,3,4,5,6,7,8])
marks = np.array([35,43,55,50,65,70,85,90]) 

# add bias term
X =np.c_[np.ones(len(hours)),hours]
y = marks

#OLS
theta = np.linalg.inv(X.T @ X) @ X.T @ y
theta_0,theta_1 =theta
#prediction line
hours_line = np.linspace(0,9,100)
X_line = np.c_[np.ones(len(hours_line)), hours_line]
marks_pred = X_line @ theta
#model evaluation
y_hat = X @ theta
mse = np.mean((y_hat -y)**2)
#visualization
plt.figure()
plt.scatter(hours, marks)
plt.plot(hours_line, marks_pred)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Student Marks Prediction using OLS")
plt.show()

theta, mse
