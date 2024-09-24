#
# ### **Exercise 1: Creating DataFrame from Scratch**
# 1. Create a DataFrame with the following columns: `"Product"`, `"Category"`, `"Price"`, and `"Quantity"`. Use the following data:
#    - Product: `['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone']`
#    - Category: `['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics']`
#    - Price: `[80000, 1500, 20000, 3000, 40000]`
#    - Quantity: `[10, 100, 50, 75, 30]`
# 2. Print the DataFrame.
import pandas as pd

data = {
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Category": ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    "Price": [80000, 1500, 20000, 3000, 40000],
    "Quantity": [10, 100, 50, 75, 30]
}
df = pd.DataFrame(data)
print(df)

# ### **Exercise 2: Basic DataFrame Operations**
# 1. Display the first 3 rows of the DataFrame.
# 2. Display the column names and index of the DataFrame.
# 3. Display a summary of statistics (mean, min, max, etc.) for the numeric columns in the DataFrame.
print(df.head(3))
print(df.columns)
print(df.index)
print(df.describe())

# ### **Exercise 3: Selecting Data**
# 1. Select and display the `"Product"` and `"Price"` columns.
# 2. Select rows where the `"Category"` is `"Electronics"` and print them.
print(df[['Product', 'Price']])
print(df[df['Category'] == 'Electronics'])

# ### **Exercise 4: Filtering Data**
# 1. Filter the DataFrame to display only the products with a price greater than `10,000`.
# 2. Filter the DataFrame to show only products that belong to the `"Accessories"` category and have a quantity greater than `50`.
print(df[df['Price'] > 10000])
print(df[(df['Category'] == 'Accessories') & (df['Quantity'] > 50)])

# ### **Exercise 5: Adding and Removing Columns**
# 1. Add a new column `"Total Value"` which is calculated by multiplying `"Price"` and `"Quantity"`.
# 2. Drop the `"Category"` column from the DataFrame and print the updated DataFrame.
df['Total Value'] = df['Price'] * df['Quantity']
df = df.drop(columns=['Category'])
print(df)

# ### **Exercise 6: Sorting Data**
# 1. Sort the DataFrame by `"Price"` in descending order.
# 2. Sort the DataFrame by `"Quantity"` in ascending order, then by `"Price"` in descending order (multi-level sorting).
print(df.sort_values(by='Price', ascending=False))
print(df.sort_values(by=['Quantity', 'Price'], ascending=[True, False]))

# ### **Exercise 7: Grouping Data**
# 1. Group the DataFrame by `"Category"` and calculate the total quantity for each category.
# 2. Group by `"Category"` and calculate the average price for each category.
print(df.groupby('Category')['Quantity'].sum())
print(df.groupby('Category')['Price'].mean())

# ### **Exercise 8: Handling Missing Data**
# 1. Introduce some missing values in the `"Price"` column by assigning `None` to two rows.
# 2. Fill the missing values with the mean price of the available products.
# 3. Drop any rows where the `"Quantity"` is less than `50`.
df.loc[1, 'Price'] = None
df.loc[3, 'Price'] = None
mean_price = df['Price'].mean()
df = df['Price'].fillna(mean_price)

# ### **Exercise 9: Apply Custom Functions**
# 1. Apply a custom function to the `"Price"` column that increases all prices by 5%.
# 2. Create a new column `"Discounted Price"` that reduces the original price by 10%.
df['Price'] = df['Price'].map(lambda x: x * 1.05)
df['Discounted Price'] = df['Price'] * 0.90

# ### **Exercise 10: Merging DataFrames**
# 1. Create another DataFrame with columns `"Product"` and `"Supplier"`, and merge it with the original DataFrame based on the `"Product"` column.
df_suppliers = pd.DataFrame({
    "Product": ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    "Supplier": ['Supplier1', 'Supplier2', 'Supplier3', 'Supplier4', 'Supplier5']
})
df_merged = pd.merge(df, df_suppliers, on='Product')
