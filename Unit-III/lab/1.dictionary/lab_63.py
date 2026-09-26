# empty dictionary
d={}

student = {"name":"Lavneesh", "age":21, "course":"BCA", "perc":90}

# print(student)
print(student["name"],student["age"],student["course"],student["perc"])

# keys() method returns a view object that displays a list of all the keys in the dictionary.
print(student.keys())

# values() method returns a view object that displays a list of all the values in the dictionary.
print(student.values())

# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(student.items())

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)