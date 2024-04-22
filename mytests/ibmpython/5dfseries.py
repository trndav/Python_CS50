import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
print(type(s))


import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)


print(df['Name'])  # Access the 'Name' column


print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])     


unique_dates = df['Age'].unique()
print(unique_dates)

high_above_102 = df[df['Age'] > 25]
print(high_above_102)

df.to_csv("test_saving_csv", index=False)