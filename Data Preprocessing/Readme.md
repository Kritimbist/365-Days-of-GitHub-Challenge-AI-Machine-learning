# Data Preprocessing
Today I learned about data preprocessing, which is one of the most important steps in any machine learning project. Raw data is usually messy, incomplete, and inconsistent, so preprocessing is needed to make the data suitable for training a model.

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/e7bd838c-5647-4b2e-aae9-d706be8733e5" />

## Data Cleaning

I learned that data cleaning is the process of fixing errors and inconsistencies in raw data so it becomes reliable and usable for analysis or machine learning. Real-world data is often messy, containing missing values, duplicate records, incorrect entries, and outliers. If I do not clean the data properly, even a good model can give poor and misleading results.

### Handling Missing Values
First, I learned how to handle missing values by either removing rows with missing data or filling them using mean, median, or mode, depending on the situation. This helps prevent errors during training.

To understand the process of handling missing value ,I first created a small dataset with missing values using NaN. Then I checked how many missing values were present in each column. For numerical columns like Age and Salary, I replaced missing values with the mean of the column. For the categorical column Department, I filled the missing value using the mode, which is the most frequent category.
- Output:

  <img width="584" height="480" alt="image" src="https://github.com/user-attachments/assets/7d15a4f3-ea0d-4155-aa19-b974eb239e2c" />

  - Source :https://www.geeksforgeeks.org/data-science/data-preprocessing-in-data-mining/
  - Code :https://github.com/Kritimbist/365-Days-of-GitHub-Challenge-AI-Machine-learning/blob/main/Data%20Preprocessing/code/Handle_missing_Value.py

## Fixing incorrect or inconsistent data
I learned that incorrect or inconsistent data can seriously affect model performance. These issues usually appear as impossible values, inconsistent category names, or wrong data formats. Before training a model, I need to identify and fix these problems so the data becomes reliable.
###  Common Problems I Fixed
- Negative values where they should not exist (e.g., age = -5)
- Different spellings for the same category (e.g., "Male", "male", "M")
- Extra spaces or mixed cases in text data
- Numerical values stored as strings

  <img width="705" height="344" alt="image" src="https://github.com/user-attachments/assets/136ec75c-b596-4cbb-b1a8-05d4b3690bf9" />


I first identified incorrect values in the Age column, such as negative numbers and unrealistic ages, and replaced them with NaN. Then I fixed inconsistent values in the Gender column by removing extra spaces, converting all text to lowercase, and mapping different representations to a single standard format. Finally, I converted the Salary column from text to numeric values, forcing invalid entries to become missing values so they can be handled later. This process helped me make the dataset consistent and reliable.
