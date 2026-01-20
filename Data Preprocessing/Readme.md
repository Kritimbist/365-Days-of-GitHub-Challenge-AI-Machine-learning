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
  - Code :
