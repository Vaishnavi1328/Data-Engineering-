# Exercise 1: Create a List
# Create a list called fruits with the following items: "apple", "banana", "cherry", "date", and "elderberry".
# Print the list.
fruits=["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# Exercise 2: Access List Elements
# Print the first and last items from the fruits list.
# Print the second and fourth items from the list.
print("first:" + fruits[0] + " last:" + fruits[-1])
print("Second:" + fruits[1] + " fourth:" + fruits[3])

# Exercise 3: Modify a List
# Replace "banana" in the fruits list with "blueberry".
# Print the modified list.
fruits=['blueberry' if x == 'banana' else x for x in fruits]
print(fruits)

# Exercise 4: Add and Remove Elements
# Append "fig" and "grape" to the fruits list.
# Remove "apple" from the list.
# Print the final list.
fruits.append('fig')
fruits.append('grape')
fruits.remove('apple')
print(fruits)

# Exercise 5: Slice a List
# Slice the first three elements from the fruits list and assign them to a new list called first_three_fruits.
# Print first_three_fruits.
first_three_fruits = fruits[:3]
print(first_three_fruits)

# Exercise 6: Find List Length
# Find and print the length of the fruits list.
print(len(fruits))

# Exercise 7: List Concatenation
# Create a second list called vegetables with the following items: "carrot", "broccoli", "spinach".
# Concatenate the fruits and vegetables lists into a new list called food.
# Print the food list.
vegetables = ["carrot", "broccoli", "spinach"]
food = fruits +vegetables
print(food)

# Exercise 8: Loop Through a List
# Loop through the fruits list and print each item on a new line.
for fruit in fruits:
    print(fruit)

# Exercise 9: Check for Membership
# Check if "cherry" and "mango" are in the fruits list. Print a message for each check.
if 'cherry' in fruits:
    print("cherry is found")
else:
    print("cherry is not found")

if 'mango' in fruits:
    print("mango is found")
else:
    print("mango is not found")

# Exercise 10: List Comprehension
# Use list comprehension to create a new list called fruit_lengths that contains the lengths of each item in the fruits list.
# Print the fruit_lengths list.
fruit_lengths  = [len(fruit) for fruit in fruits]
print(fruit_lengths)

# Exercise 11: Sort a List
# Sort the fruits list in alphabetical order and print it.
# Sort the fruits list in reverse alphabetical order and print it.
print(sorted(fruits))
print(sorted(fruits,reverse=True))

# Exercise 12: Nested Lists
# Create a list called nested_list that contains two lists: one with the first three fruits and one with the last three fruits.
nested_list = []
nested_list.append(first_three_fruits)
last_three_fruits = fruits[-3:]
nested_list.append(last_three_fruits)
print(nested_list)
# Access the first element of the second list inside nested_list and print it.
print(nested_list[1][0])

# Exercise 13: Remove Duplicates
# Create a list called numbers with the following elements: [1, 2, 2, 3, 4, 4, 4, 5].
# Remove the duplicates from the list and print the list of unique numbers.
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
numbers = list(unique_numbers)
print(numbers)

# Exercise 14: Split and Join Strings
# Split the string "hello, world, python, programming" into a list called words using the comma as a delimiter.
# Join the words list back into a string using a space as the separator and print it.
str = "hello, world, python, programming"
words = str.split(',')
print(words)
result = ' '.join(words)
print(result)