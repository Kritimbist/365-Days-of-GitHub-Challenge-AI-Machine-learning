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

## Removing Duplicate Data
I learned that duplicate data means repeated rows that contain the same information. These duplicates can occur due to data collection errors, merging datasets, or repeated entries. If I do not remove duplicates, the model may learn biased patterns because the same data is counted multiple times.

I first created a dataset that contained duplicate rows. I used the duplicated() function to check how many duplicate records were present in the dataset. Then I removed those duplicates using the drop_duplicates() method. This ensured that each record appeared only once, making the dataset more accurate and reliable for further analysis or machine learning.

<img width="615" height="279" alt="image" src="https://github.com/user-attachments/assets/220ebae7-618f-4d5d-a28f-8172a6d2ccb2" />
<img width="587" height="176" alt="image" src="https://github.com/user-attachments/assets/82fed956-1ecd-4db7-bc03-3d4a8c923d56" />


## Handling outliers
I learned that outliers are extreme or unusual values that do not follow the general pattern of the data. Outliers can occur due to data entry errors, measurement issues, or rare but valid cases. If I do not handle outliers properly, they can distort the model and affect predictions.

I learned how to detect outliers using the IQR (Interquartile Range) method. I first created a simple dataset of house prices and intentionally added extreme values to represent outliers. I calculated the first quartile (Q1) and third quartile (Q3), then computed the IQR as the difference between them. Using the standard 1.5 × IQR rule, I defined lower and upper bounds and classified data points outside this range as outliers. Finally, I visualized the normal values and detected outliers using a scatter plot along with the IQR boundaries.


<img width="941" height="630" alt="image" src="https://github.com/user-attachments/assets/263264e6-ba4b-4958-80f1-65db328ccb36" />


## Correcting data types
Today I learned how to correct data types as an important step in data cleaning. When I load a real-world dataset, many columns are not in the correct format. Some numerical values are stored as strings, dates appear as plain text, and categorical values are treated as generic objects. If I do not fix these issues, data analysis and machine learning models may produce incorrect results.

I created a random dataset where numeric, boolean, and date values were incorrectly stored as text. I first checked the existing data types and then converted numeric columns using to_numeric, fixed boolean values using mapping, and converted the date column to datetime format. This process ensured my dataset had correct and meaningful data types, making it ready for analysis or machine learning.

<img width="667" height="316" alt="image" src="https://github.com/user-attachments/assets/40dd8b5c-9868-47cc-a8f9-304c1bf7ee86" />



# Data Integration
It involves merging data from various sources into a single, unified dataset. It can be challenging due to differences in data formats, structures, and meanings. Techniques like record linkage and data fusion help in combining data efficiently, ensuring consistency and accuracy.

## Record Linkage
Record linkage is the process where I match and connect records from different datasets that refer to the same entity. I handle differences in names, formats, or missing identifiers by comparing common attributes such as phone numbers, dates, or text similarity.

<img width="1098" height="521" alt="image" src="https://github.com/user-attachments/assets/faa0953e-243f-4400-b753-86c9b401b809" />

<img width="1047" height="506" alt="image" src="https://github.com/user-attachments/assets/65ac965a-3627-49cc-b0b8-b80fbd2ca470" />

<img width="977" height="676" alt="image" src="https://github.com/user-attachments/assets/beff9edb-1db2-4b06-9ce5-2c60d305bacf" />

In this code, I created two small datasets to represent data coming from different sources. The first dataset contains names and phone numbers, while the second dataset contains similar information but with different column names and slightly different name formats. I then used pd.merge() to perform record linkage by matching the phone number column from the first dataset with the contact column from the second dataset. By doing this, I linked records that refer to the same person based on a common identifier, even though their names are written differently. This allowed me to combine related information from both datasets into a single unified view.



