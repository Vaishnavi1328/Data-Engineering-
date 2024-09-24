# set-mutable,unorderd,duplicates not allowed
set={'apple','orange','cherry'}
# add
set.add('pineapple')
print(set)
# remove
set.remove('apple')
print(set)
# length
print(len(set))
# iteration
for fruit in set:
    print(fruit)
# checking if element is present in set
print("if banana in set?",'banana' in set)
print("if cherry in set?",'cherry' in set)
