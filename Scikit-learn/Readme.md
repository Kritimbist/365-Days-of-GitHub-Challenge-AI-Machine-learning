# Supervised Learning

## Linear Models


A **Linear Model** is a fundamental machine learning and statistical model that represents the relationship between input features and an output as a **linear combination**. It is widely used due to its simplicity, interpretability, and efficiency.

---

## 📐 Mathematical Formulation

### ➤ General Linear Model
$$[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n + \varepsilon
]
$$
**Where:**

* ( y ) is the target (dependent) variable
* ( x_1, x_2, \ldots, x_n ) are input (independent) features
* ( \beta_0 ) is the intercept (bias term)
* ( \beta_1, \beta_2, \ldots, \beta_n ) are model parameters (weights)
* ( \varepsilon ) represents the error or noise

---

### ➤ Vectorized Form

$$ [
\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}
] $$

Where:

* ( \mathbf{X} ) is the feature matrix
* ( \boldsymbol{\beta} ) is the parameter vector

---

### ➤ Prediction Function (Machine Learning Form)

$$ [
\hat{y} = \mathbf{w}^T \mathbf{x} + b
] $$

* ( \mathbf{w} ) is the weight vector
* ( b ) is the bias

---

## 📉 Loss Function (Mean Squared Error)

$$ [
\mathcal{L}(y, \hat{y}) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
] $$

The model is trained by minimizing this loss function.

---

## ⭐ Key Characteristics

* Simple and fast to train
* Easy to interpret coefficients
* Works well when relationship is approximately linear
* Sensitive to outliers and multicollinearity

---

## 📌 Applications

* Regression problems
* Baseline models in machine learning
* Economics, finance, and scientific modeling

---

##  Ordinary Least Squares
Today i learnt about OLS , OLS is used to learn a linear relationship between input features and a target value.

we know that the linear equation :
$$y = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_n x_n + \epsilon$$
where,

- y → actual output

- x → input features

- θ → parameters (weights) we want to learn

- ε → noise


OLS asks:
“Which values of θ make my predictions as close as possible to the real data?”


<img width="1400" height="870" alt="image" src="https://github.com/user-attachments/assets/64f3fbfc-bc58-47e7-9868-48a5ce46f736" />

## Ridge regression 
Today I learned about Ridge Regression in machine learning. Ridge regression is an improved version of linear regression (OLS). In ordinary least squares, the model tries to reduce the error as much as possible, but sometimes this causes the model to give very large values to the coefficients, especially when the features are highly related to each other.

Ridge regression solves this problem by adding a penalty term to the cost function. This penalty controls the size of the coefficients and prevents overfitting.
The cost function of ridge regression is:

$\text{Cost} = \sum (y - \hat{y})^2 + \lambda \sum \theta^2$

- Squared Error:$(y - \hat{y})^2$ renders as $(y - \hat{y})^2$
- L2 Regularization Term:$\sum \theta^2$ renders as $\sum \theta^2$
- Regularization Parameter (Lambda):$\lambda$ renders as $\lambda$

  The main idea of ridge regression is to reduce model complexity and improve prediction on new data. It is mainly used when the dataset has multicollinearity or when the linear regression model is overfitting.

  I applied Ridge Regression to predict product sales using advertising budget. Ordinary least squares tries to fit the data closely and may give higher coefficient values. Ridge regression adds a regularization term that reduces the magnitude of coefficients.

In the graph, the Ridge regression line is smoother and less steep than the OLS line. This shows that Ridge regression controls model complexity and reduces overfitting, especially when data contains noise.

<img width="708" height="573" alt="image" src="https://github.com/user-attachments/assets/394663a2-3aff-4d83-928f-53479fe8845c" />


