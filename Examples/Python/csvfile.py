#csv file
# writing data into csv file
import csv
data = [['Nme','Age'],['Alice',25],['Bob',30]]
with open("D:/Users/Downloads/data.csv",'w',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)

# # reading data from csv file
with open("D:/Users/Downloads/data.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# json - to communicate between language
import json
# writing data into json
data = {'name':'Alice','age':30,'city':'New York'}
with open("D:/Users/Downloads/data.json",'w') as file:
    json.dump(data,file)

# reading data from json
with open("D:/Users/Downloads/data.json",'r') as file:
    result_data = json.load(file)
    print(result_data)

