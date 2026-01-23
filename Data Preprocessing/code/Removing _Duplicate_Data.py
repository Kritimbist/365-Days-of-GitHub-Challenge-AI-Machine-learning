import pandas as pd

# Sample dataset with duplicate rows
data = {
    "Student_ID": [1, 2, 3, 3, 4, 2],
    "Name": ["Amit", "Sara", "John", "John", "Nina", "Sara"],
    "Score": [85, 90, 78, 78, 88, 90]
}
df = pd.DataFrame(data)
print("Orginal Dataset")
print(df)
#check the number of duplicated rows

print("\nDuplicate Rows :")
print(df.duplicated().sum())

#remove duplicated rows
df_cleaned = df.drop_duplicates()

print("\nData after removing duplicates:")
print(df_cleaned)
