#  365 Days Challenge — AI & Machine learning
<img width="860" height="535" alt="image" src="https://github.com/user-attachments/assets/d66a55d6-c4e2-45f1-8bff-c586d22031dc" />



> “Somewhere, something incredible is waiting to be known.” — Carl Sagan  

Welcome to my **365 Days of GitHub Challenge**, where I’ll combine my passion for **Machine Learning** 🤖  to learn, build, and share projects every single day for one year!



##  Tools & Libraries

- **Languages:** Python  
- **Frameworks:** PyTorch, TensorFlow, Scikit-learn  
- **Visualization:** Matplotlib, Plotly, Seaborn  
- **Dev Tools:** Git, GitHub, Jupyter, VS Code  


## Day 001 : Data Distribution using python

Today i learn about the concept of data distribution and some of it's examples .  Data distribution show how data values are spread out and it helps in :

- Detect outliers
- See if your data is balanced or skewed
- Decide whether you need normalization or transformation
- Detect imbalanced classes in classification problems

I've use  python module Numpy, where we can create random data sets of any size.
# some of the examples  of data distribution

<img width="964" height="770" alt="image" src="https://github.com/user-attachments/assets/57749f77-cf2c-46f3-b43a-44510f7004f1" />




## Day 002 : Visualizing Data Distribution using python

Today i learn about how to visualize the distributed data . 


## 📈 Visualization Types


###  Histogram
A **histogram** shows how data is distributed by grouping values into bins.
We will use the Python module Matplotlib to draw a histogram.
# sample example of histogram:
<img width="846" height="702" alt="image" src="https://github.com/user-attachments/assets/ccce542b-ba96-441a-b9a3-e128832cc591" />



##  Normal Distribution 

A **normal distribution** is characterized by:
- A **mean (μ)** — the center of the curve  
- A **standard deviation (σ)** — controls how spread out the data is  

The formula for the probability density function is:

A Probability Density Function (PDF) is a mathematical function that tells you how likely a continuous outcome (like height, time, or temperature) is to fall within a certain range.

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

# Simple example of visualizing noram distribution:
<img width="762" height="689" alt="image" src="https://github.com/user-attachments/assets/cfdae9be-9ef1-4375-934f-958fc60c7149" />



##  scatter plot
A scatter plot is a diagram where each value in the data set is represented by a dot.
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/168d08ea-cf6f-43cb-aa75-625004600152" />

The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
- x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
- y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

Use the scatter() method to draw a scatter plot diagram.

# Simple example of scatter plot :

<img width="907" height="726" alt="image" src="https://github.com/user-attachments/assets/c2e18951-9daf-44a9-8334-456b80893b05" />

## Random Data Distributions
In Machine Learning the data sets can contain thousands-, or even millions, of values.
You might not have real world data when you are testing an algorithm, you might have to use randomly generated values.

Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
The first array will have the mean set to 5.0 with a standard deviation of 1.0.
The second array will have the mean set to 10.0 with a standard deviation of 2.0:

simple examples of random data distribution :
<img width="904" height="705" alt="image" src="https://github.com/user-attachments/assets/eb810ce1-a45e-417d-a215-b7a58628f7ad" />

# Regression

In machine learning, regression is a type of supervised learning technique used to predict a continuous numerical value.
Think of it as finding the mathematical relationship between a set of input features (like the size of a house, number of bedrooms, and location) and a continuous output (like its final sale price). The goal is to build a model that can take new, unseen input features and make an accurate prediction about the output.

Supervised learning is a type of machine learning where the model learns from labeled data — meaning we already know the input and the correct output.
You can think of it like a teacher guiding a student :
- The teacher gives examples (inputs) and the correct answers (labels).
- The student (model) learns the pattern between them.
- Later, the student can predict answers for new examples.
  
Continuous numerical values are numbers that can take any value within a range — including fractions and decimals.

Think of them as values that change smoothly instead of jumping from one value to another.

🔹 Examples:

Height → 165.4 cm, 170.2 cm, 171.8 cm

Weight → 55.5 kg, 55.55 kg, 56.1 kg

Temperature → 25.1°C, 25.15°C, 25.2°C

Time → 2.5 seconds, 2.55 seconds, 2.556 seconds

These can have infinite possible values between any two numbers.

<img width="2048" height="1939" alt="image" src="https://github.com/user-attachments/assets/2ff7031f-6d7d-4c4d-9e07-2f289cafdf89" />

## 📈 Common Types of Regression Algorithms
While all regression models aim to predict a number, they use different methods to find the underlying patterns in the data.

### Linear Regression
This is the simplest and most common type. It assumes a linear relationship (a straight line) between the input variables (X) and the output variable (Y).


# Simple Linear Regression
This is used when you have one independent variable (X) to predict a continuous dependent variable (Y). The goal is to find the best-fitting straight line for the data.The formula for the regression line is:
$$
y = b_0 + b_1 * x + \epsilon
$$

Where:  
- \( y \) = Dependent variable (what we want to predict)  
- \( x \) = Independent variable (input feature)  
- \( b_0 \) = Intercept (value of \( y \) when \( x = 0 \))  
- \( b_1 \) = Slope (how much \( y \) changes with one unit increase in \( x \))  
- \( \epsilon \) = Error term (difference between actual and predicted value)

<img width="3000" height="2000" alt="image" src="https://github.com/user-attachments/assets/efc78c04-9f64-494d-beb9-7c4eaeb0bfd4" />


# Simple example for simple linear regression :
<img width="1215" height="704" alt="image" src="https://github.com/user-attachments/assets/6be23bcf-e22e-4bbd-8b2a-fc76eedb906b" /> <img width="1052" height="768" alt="image" src="https://github.com/user-attachments/assets/398aab09-a5c9-458c-8901-42342a50d426" />
<img width="963" height="710" alt="image" src="https://github.com/user-attachments/assets/ac13fc52-9309-497b-b0d6-5084d1948321" />

##  Code Breakdown: 
- We create two numpy arrays. X is our input feature, and y is our target output.Important: scikit-learn models expect the X data to be a 2D array, even for simple regression with one feature. X.reshape(-1, 1) converts our 1D array [1, 2, 3...] into a 2D array [[1], [2], [3]...].
- Create and Train the Model:model = LinearRegression(): We create an instance of the regression model.model.fit(X, y): This is the "training" step. The model "learns" the best possible straight line to fit the X and y data points by finding the optimal values for the slope ($b_1$) and intercept ($b_0$).
- View the Results:model.intercept_: This gives you the calculated intercept ($b_0$) from the formula.model.coef_: This gives you an array of coefficients. Since this is simple linear regression, we only have one, coef_[0], which is our slope ($b_1$).
- Make Predictions:model.predict(X): We use the trained model to predict the y-values for our original X-values. This gives us the points that lie directly on the red line.
- Plot the Results:plt.scatter(X, y): This plots our original, "real" data points as blue dots.plt.plot(X, y_pred): This plots the predicted values as a red line, which is the final regression line.

## Multiple Linear Regression :

While simple linear regression uses one variable to make a prediction (e.g., Size $\to$ Price), multiple linear regression is a more powerful technique that uses two or more independent variables to predict a single continuous output.This is much more realistic for most real-world problems. For example, a house's price isn't just based on its size; it's also based on the number of bedrooms, the age of the house, the neighborhood, etc.

## Formula for Multiple Linear Regression
The formula is a straightforward extension of the one for simple linear regression. You just add a new "coefficient + variable" term for each new feature.The general formula is:
$$y = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_n + \epsilon$$

- $y$ (Dependent Variable): The value we want to predict (e.g., House Price).
- $x_1, x_2, \dots, x_n$ (Independent Variables): The features we use to predict (e.g., $x_1$ = Size, $x_2$ = Num of Bedrooms, $x_3$ = House Age).
- $b_0$ (The Intercept): The base value of $y$ when all features ($x_1, x_2, \dots$) are zero. (The "base price" of a house with 0 size, 0 bedrooms, etc.).$b_1, b_2, \dots, b_n$ (The Coefficients): This is the most important part. Each coefficient represents the "strength" and "direction" of its corresponding feature's relationship with $y$.
- $\epsilon$ (Epsilon, the Error Term): The random error or noise that the model can't explain.


<img width="3410" height="2739" alt="image" src="https://github.com/user-attachments/assets/4bc6db1b-5c24-495d-97bf-2a5897b41064" />

# Simple example of Multiple Linear Regression:

<img width="1229" height="764" alt="image" src="https://github.com/user-attachments/assets/2ac4ee8c-6072-4dd8-b154-d4dba298f575" /> <img width="930" height="428" alt="image" src="https://github.com/user-attachments/assets/eb8e45cd-65cd-4cfc-8abc-0c851cc5502c" /> <img width="874" height="545" alt="image" src="https://github.com/user-attachments/assets/38dcac78-d0e8-4af0-b308-b52fee2ec96a" />

## Cost function for Linear Regression
A cost function is a mathematical formula that measures the "cost" or error of a machine learning model.

Imagine you have a scatter plot of data points, like house sizes and their prices. Your goal in linear regression is to draw one straight line that best fits all those points.
But how do you know which line is the "best"?
The cost function is a "score" that tells you how bad your line is. A high score means your line is a terrible fit. A low score means your line is a great fit.
Your goal is to find the line that gives you the lowest possible score (the lowest "cost").
<img width="3000" height="2000" alt="image" src="https://github.com/user-attachments/assets/729daa37-0d24-4d03-9dc9-be133302d4fd" />
In this image, the red vertical lines represent the errors (residuals) for each point. The cost function calculates the average of the squares of the lengths of all these red lines.

### The Formula (Mean Squared Error)

The most common cost function for linear regression is the Mean Squared Error (MSE).
$$J = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- Let's break that down:
- $J$: This is just a common name for the cost function.
- $n$: The total number of data points you have.
- $\sum_{i=1}^{n}$: A fancy "sum" symbol. It just means "add up the following for every single point, from the 1st point to the $n$-th point.
- $y_i$: The actual 'y' value (e.g., the true price) of the $i$-th data point.
- $\hat{y}_i$: (pronounced "y-hat") The predicted 'y' value from your line for the $i$-th data point.
- $(y_i - \hat{y}_i)$: This is the error (the vertical distance we saw in the diagram).
- $(y_i - \hat{y}_i)^2$: This is the squared error.


## Visualizing the Cost Function Itself

This is a key concept. Your line is defined by its slope ($m$) and its y-intercept ($b$).
- If you pick a bad $m$ and $b$, your squared errors will be huge, and your Cost ($J$) will be high.
- If you pick the perfect $m$ and $b$, your squared errors will be tiny, and your Cost ($J$) will be at its absolute minimum.

  If you were to plot every possible value of $m$ and $b$ against the Cost ($J$) they produce, you would get a 3D bowl shape.
  <img width="3688" height="1876" alt="image" src="https://github.com/user-attachments/assets/2a778926-e6ca-4977-a8b1-ce1fc6ad2792" />
  The bottom of the bowl is the lowest cost (minimum error).The $m$ and $b$ values at that very bottom point are the parameters for your best-fit line!The whole process of "training" a model is just an algorithm (like Gradient Descent) "walking" down the side of this bowl to find the bottom.
  <img width="819" height="481" alt="image" src="https://github.com/user-attachments/assets/93c1acea-558b-43e0-b95a-5aa669a86061" />

  ## Simple Code Example (Python)
  
<img width="982" height="745" alt="image" src="https://github.com/user-attachments/assets/f646c084-0bf7-4e01-bcfa-a0503e3d1041" /> <img width="907" height="619" alt="image" src="https://github.com/user-attachments/assets/765a58dd-b95f-4b85-af24-009f406296ef" />
<img width="1050" height="652" alt="image" src="https://github.com/user-attachments/assets/d0015137-9f22-41ed-b28e-fbb5b33a04c0" />

## Gradient Descent 
Gradient Descent is an iterative optimization algorithm used to minimize a cost (loss) function by adjusting model parameters in the direction of the negative gradient.

In simple terms:

Keep taking small steps downhill until you reach the lowest point.
<img width="569" height="302" alt="image" src="https://github.com/user-attachments/assets/f376a342-0f5c-4bf6-8928-31023a6a635c" />

### Mathematical Intuition

<img width="305" height="97" alt="image" src="https://github.com/user-attachments/assets/1475e4f5-485f-477e-aa52-25173851ff43" />

Where:

- θ = model parameter

- α (alpha) = learning rate

- ∂J/∂θ = gradient of the cost function

<img width="657" height="136" alt="image" src="https://github.com/user-attachments/assets/3fc4611b-4da0-45d2-93f8-3daabb4da985" />

<img width="636" height="364" alt="image" src="https://github.com/user-attachments/assets/68869151-5b3e-4c85-8c49-5511e37f665a" />
On a side note, we should adjust our parameter α αalpha to ensure that the gradient descent algorithm converges in a reasonable time. Failure to converge or too much time to obtain the minimum value imply that our step size is wrong.
<img width="663" height="365" alt="image" src="https://github.com/user-attachments/assets/4d52bba4-ae89-497e-99af-01ab5064c746" />

<img width="654" height="362" alt="image" src="https://github.com/user-attachments/assets/0e357748-4dff-43e4-ae39-3f4a7ca16b73" />

## Gradient Descent For Linear Regression
When specifically applied to the case of linear regression, a new form of the gradient descent equation can be derived. We can substitute our actual cost function and our actual hypothesis function and modify the equation to :

<img width="770" height="220" alt="image" src="https://github.com/user-attachments/assets/3f48e173-8326-4d87-891b-03cee8f77e8d" />

<img width="1083" height="392" alt="image" src="https://github.com/user-attachments/assets/aacc5f95-0803-4381-a10b-c28988f8f939" />
The point of all this is that if we start with a guess for our hypothesis and then repeatedly apply these gradient descent equations, our hypothesis will become more and more accurate.

So, this is simply gradient descent on the original cost function J. This method looks at every example in the entire training set on every step, and is called batch gradient descent. Note that, while gradient descent can be susceptible to local minima in general, the optimization problem we have posed here for linear regression has only one global, and no other local, optima; thus gradient descent always converges (assuming the learning rate α is not too large) to the global minimum. Indeed, J is a convex quadratic function. Here is an example of gradient descent as it is run to minimize a quadratic function.
<img width="316" height="240" alt="image" src="https://github.com/user-attachments/assets/36837457-d80d-4531-8265-5309feb9f254" />

The ellipses shown above are the contours of a quadratic function. Also shown is the trajectory taken by gradient descent, which was initialized at (48,30). The x’s in the figure (joined by straight lines) mark the successive values of θ that gradient descent went through as it converged to its minimum.


## Simple mini-project of linear regression
"Today, I completed a mini-project predicting student marks using Ordinary Least Squares (OLS). I utilized a small dataset of study hours and marks to train the model and visualized the correlation with a scatter plot. The source code is organized in a dedicated folder, and the visualization can be seen below."

- source: https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html
- Source code : https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/python%20for%20machine%20learning/sutdent_marks_prediction.py



<img width="826" height="611" alt="image" src="https://github.com/user-attachments/assets/9fc5c62d-00a3-43cb-b65d-6f652fd341c0" />

## Ridge Regression
Today I applied Ridge Regression to predict product sales using advertising budget. Ordinary least squares tries to fit the data closely and may give higher coefficient values. Ridge regression adds a regularization term that reduces the magnitude of coefficients.

In the graph, the Ridge regression line is smoother and less steep than the OLS line. This shows that Ridge regression controls model complexity and reduces overfitting, especially when data contains noise.
- source : https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification
- code : https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/Scikit-learn/code/Ridge_Regres.py
  
- Output :

<img width="702" height="572" alt="image" src="https://github.com/user-attachments/assets/f2fc47e3-afee-4a2c-8031-c0d790f6a222" />

## Lasso Regression

Today I learned about Lasso Regression in machine learning. Lasso is a type of linear regression that adds L1 regularization to the ordinary least squares loss. Unlike OLS and Ridge regression, Lasso can shrink coefficients to exactly zero, which helps in feature selection and reduces overfitting.

  <img width="766" height="237" alt="image" src="https://github.com/user-attachments/assets/64b0669e-e5bc-4e75-8b18-16212a601f37" />


To understand Lasso clearly, I took a simple example of engine size and fuel consumption. I first applied Ordinary Least Squares (OLS) to see how a normal linear regression fits the data without any regularization. OLS tries to fit the data closely and is sensitive to noise.

After that, I applied Lasso regression with a higher regularization value. In the code, I used Lasso to penalize large coefficients. Because of the L1 penalty, the slope of the line was reduced and became zero, meaning the model ignored the feature completely.

Finally, I visualized both OLS and Lasso prediction lines using a plot. From the graph, I could clearly see that OLS fits the noisy data more aggressively, while Lasso produces a simpler model by shrinking the coefficient and reducing the effect of the feature. This helped me understand how Lasso regression controls model complexity and performs feature selection.

   
<img width="780" height="642" alt="image" src="https://github.com/user-attachments/assets/596d9228-5d51-4070-839e-d77afd0980cc" />

- Source :https://scikit-learn.org/stable/modules/linear_model.html#lasso
- Code:https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/Scikit-learn/code/Lasso_Regg.py



## Multi-task Lasso
I implemented Multi-Task Lasso regression using a simple example of engine size as the input feature. I created two related target variables: fuel consumption and CO₂ emission. Since both outputs depend on the same feature, this makes it a good example for multi-task learning.

First, I generated a synthetic dataset with some noise to make it realistic. Then I combined both target variables into a single matrix so the model could learn them together. After that, I trained a MultiTaskLasso model with a regularization parameter (alpha = 0.5), which applies shared L1 regularization across both tasks.

Next, I generated predictions for new engine size values and plotted the results. In the visualization, the scatter points represent the original data, and the straight lines represent the predictions made by the Multi-Task Lasso model for both tasks. From the plot, it is clear that the model learns both outputs simultaneously while using the same input feature.

This example helped me understand how Multi-Task Lasso performs joint feature selection and builds simpler, more stable models when multiple prediction tasks are related.

<img width="1105" height="637" alt="image" src="https://github.com/user-attachments/assets/63b996c9-be55-49e4-9938-7800bcffcbd7" />

- Source :https://scikit-learn.org/stable/modules/linear_model.html#lasso
- Code :https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/Scikit-learn/code/Multi_task%20lasso.py


## Least Angle Regression
I implemented Least Angle Regression (LARS) using a simple synthetic dataset. I created one input feature and a target variable with some added noise to simulate real-world data. This helps in understanding how LARS behaves when the data is not perfectly linear.

After creating the dataset, I trained a LARS model using scikit-learn. LARS starts with all coefficients set to zero and then gradually moves the coefficient in the direction of the feature that is most correlated with the target variable. Since this example has only one feature, LARS quickly selects it and fits a straight line to the data.

Next, I generated predictions for new input values and visualized the results. In the plot, the scatter points represent the original data, while the straight line represents the prediction made by the LARS model. The visualization clearly shows how LARS fits a linear relationship while following a step-by-step feature selection approach.

This example helped me understand how LARS efficiently builds linear models and why it is closely related to Lasso regression, especially in high-dimensional datasets.


<img width="743" height="600" alt="image" src="https://github.com/user-attachments/assets/01b6d0a9-5150-4324-b971-98b4b17d55e7" />

- Source:https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression
- Code :https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/Scikit-learn/code/LARS.py
