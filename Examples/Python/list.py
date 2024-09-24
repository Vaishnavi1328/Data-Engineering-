
#list
empty_list=[]
numbers=[1,2,3,4,5]
mixes_list=[1,3.14,'Hello']

#list operations
# append
numbers.append(6)
print(numbers)
#insert
numbers.insert(0,20)
print(numbers)
#extend
numbers.extend([7,8,9])
# numbers.extend(2) error:'int' object is not iterable.list only allowed
print(numbers)
# remove - by element
numbers.remove(20)
print(numbers)
# pop - remove by index
popped_element = numbers.pop(2)#index
print(numbers)
print("Removed element:",popped_element)
# slicing
first_three = numbers[:3]
middle_two = numbers[2:5]
last_two = numbers[-2:]
print(last_two)
# iterating
for i in numbers:
    print(i)
# creating of list of squares using list comprehension
square = [x**2 for x in range(6)]
print(square)