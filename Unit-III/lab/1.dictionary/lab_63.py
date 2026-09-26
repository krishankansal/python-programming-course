# Lab No. 63: Introduction to Dictionaries
#
# Objective:
# To understand dictionaries, create key-value pairs, access dictionary
# elements, and use keys(), values(), and items() methods.

# Program

# Creating an empty dictionary
d = {}

# Creating a dictionary with student information
student = {
    "name": "Lavneesh",
    "age": 21,
    "course": "BCA",
    "perc": 90
}

print(student["name"], student["age"], student["course"], student["perc"])

# Displaying all keys
print(student.keys())

# Displaying all values
print(student.values())

# Displaying all key-value pairs
print(student.items())

# Iterating through dictionary keys
for key in student.keys():
    print(key)

# Iterating through dictionary values
for value in student.values():
    print(value)

# Iterating through key-value pairs
for key, value in student.items():
    print(key, value)


# -----------------------------
# Key Points
# -----------------------------
# 1. A dictionary stores data in key-value pairs.
# 2. Dictionary elements can be accessed using their keys.
# 3. keys() returns a view containing the dictionary keys.
# 4. values() returns a view containing the dictionary values.
# 5. items() returns key-value pairs.
# 6. A dictionary can be traversed using a for loop.
