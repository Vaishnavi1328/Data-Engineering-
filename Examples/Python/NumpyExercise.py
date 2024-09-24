import numpy as np

# create 1 dimensional array
arr=np.array([1,2,3,4,5])
print("Array:",arr)

# reshape to 2x3 array
reshaped_array = np.arange(6).reshape(2,3)
print("Reshapes array:\n",reshaped_array)

# element wise addition
arr_add = arr+10
print("Added 10 to each element:",arr_add)

# slicing array
sliced_arr = arr[1:4] #index from 1 to 3
print("Sliced array:",sliced_arr)

# clearing data
import pandas as pd
import numpy as np
df = pd.read_csv("sample_data.csv")
print(df)

# replace a emplty string and strings with only spaces with NaN
df.replace(r'^\s*$',np.nan,regex = True,inplace=True)

# check for null values in each column
print(df.isnull().sum())

# display rows with missing data
print(df[df.isnull().any(axis=1)])#when axis is 1 row wise

# drop rows with missing values
df_cleaned = df.dropna()

print(df_cleaned)

# fill missing values in city with Unknown
df['City'] = df['City'].fillna("Unknown")
# fill missing values value in 'age' column with the median age
df['Age'] = pd.to_numeric(df['Age'].str.strip(),errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].median())


