a = 'single quote str'
b = "double quote str"
c = '''Multiline
str
'''
print(a)
print(b)
print(c)

#appending string
firstname = 'Vaishnavi'
greetWord = 'Hello'
full_greeting = greetWord+", "+firstname+"!"
print(full_greeting)

#appending using format function
fullGreeting = '{}, {}!'.format(greetWord,firstname)
greet = f"{greetWord}, {firstname}!"

#python string operations
name = ' Vaishnavi Devaraj '
print("trimmig: "+name.strip())
print("Uppercase: "+name.upper())
print(name.startswith('Vaishnavi'))
print("Replacing words: "+name.replace('Vaishnavi','Ambika'))
