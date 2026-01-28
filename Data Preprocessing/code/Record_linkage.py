import pandas as pd

# Dataset 1
df1 = pd.DataFrame({
    "name": ["Ram Sharma", "Sita Rai"],
    "phone": ["9841234567", "9812345678"]
})

# Dataset 2
df2 = pd.DataFrame({
    "full_name": ["R. Sharma", "Sita R."],
    "contact": ["9841234567", "9812345678"]
})

#Record linkage using phone no.
linked_records = pd.merge(
    df1,
    df2,
    left_on="phone",
    right_on="contact",
    how = "inner"
)
print(linked_records)
