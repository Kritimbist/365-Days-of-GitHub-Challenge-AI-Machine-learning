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


