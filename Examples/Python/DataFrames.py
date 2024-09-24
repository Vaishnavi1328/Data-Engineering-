import csv
import json

import pandas as pd
import requests
response = requests.get("https://dummyjson.com/products/1")
print(response.json())
# # Print the HTTP status code

# # dataframes

data = {
    "Name":['Amit','Priya','Vikram','Neha','Ravi'],
    "Age":[25,30,35,40,45],
    "City":['Mumbai','Delhi','Bangalore','Chennai','Pune']
}

df = pd.DataFrame(data)
print(df)

# # Acessing a single column
print("Single column")
print(df["Name"])

# # Acessing multiple column
print("Multiple column")
print(df[["Name","Age"]])

# # Acessing rows using index
print("Acessing rows using index")
print(df.iloc[0])

# # filter rows age greater than 35
filter_df = df[df['Age']>35]
print(filter_df)

# # Adding a new column salary
df['Salary'] = [50000,60000,70000,80000,90000]
print(df)

# # sort by age
sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)

# # rename the 'Name' column to 'Full Name' and 'Age' to 'Years'
df_renamed = df.rename(columns={"Name":"Full Name","Age":"Years"})
print(df_renamed)

# # Drop the 'City' column
df_dropped = df.drop(columns = ['City'])
print(df_dropped)

# # create a new column 'Seniority' based on the age
df['Seniority'] = df['Age'].apply(lambda x:'Senior' if x>35 else 'Junior')
print(df)

# # Grouped by city and calculate the average salary in each city
grouped_df = df.groupby("City")["Salary"].mean()
print(grouped_df)

# # Apply a custom function to the 'Salary' column to add a 10% bonus
def add_bonus(salary):
    return salary*1.10

df['Salary_with_bonus'] = df['Salary'].apply(add_bonus)
print(df)

df_new = pd.DataFrame({
    "Name":['Amit','Priya','Ravi'],
    "Bonus":[5000,6000,7000]
})

# # merge based on the 'Name' column
df_merged = pd.merge(df,df_new,on = 'Name',how='left')
print(df_merged)

# # create a dataframe to concatenat
df_new = pd.DataFrame({
    "Name":['Sonia','Rahul'],
    "Age":[29,31],
    "City":["Kolkata","Hyderabad"],
    "Salary":[58000,63000]
})

# # concatenat the two dataframe
df_concat = pd.concat([df,df_new],ignore_index=True)
print(df_concat)

# Data to be written to the CSV file
data = [
    ["Employee_ID", "Name", "Department", "Age", "Salary", "City"],
    [101, "Rajesh", "HR", 29, 70000, "Delhi"],
    [102, "Meena", "IT", 35, 85000, "Mumbai"],
    [103, "Suresh", "Finance", 45, 95000, "Bangalore"],
    [104, "Anita", "IT", 32, 64000, "Chennai"],
    [105, "Vijay", "Finance", 50, 120000, "Delhi"],
    [106, "Neeta", "HR", 28, 72000, "Mumbai"]
]


# # Write data to the CSV file
with open("D:/Users/Downloads/employees.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# # load csv file into dataframe
df = pd.read_csv('D:/Users/Downloads/employees.csv')

# # display the first three rows
print(df.head(3))

# show summary information about the dataFrame
print(df.info())

# # display summary statistics of numeric columns
print(df.describe())

# # filter rows where Salary is greater than 80000
high_slary_df = df[df['Salary']>80000]
print(high_slary_df)

# # sort by age in descending order
sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)

# load json data into dataFrame
df = pd.read_json('D:/Users/Downloads/employees.json')
print(df)

# add a new column 'Bonus' which is 10% of the salary
df['Bonus'] = df['Salary']*0.10
print(df)

# save the updated dataframe to a new json file
df.to_json('employees_with_bonus.json',orient='records',lines=True)


