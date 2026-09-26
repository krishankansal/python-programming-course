# Lab No. 58: Introduction to Tuples
#
# Objective:
# To understand tuples, create tuples and access their elements
# using indexing.

# Program

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits Tuple:")
print(fruits)

# Creating a tuple of numbers
numbers = (10, 20, 30, 40, 50)

print("\nNumbers Tuple:")
print(numbers)

# Creating a tuple with different data types
student = ("Rahul", 21, 85.5, True)

print("\nStudent Tuple:")
print(student)

# Checking the type of a tuple
print("\nType of student:")
print(type(student))

# Accessing the first element
print("\nFirst Fruit:")
print(fruits[0])

# Accessing the third element
print("\nThird Fruit:")
print(fruits[2])

# Accessing the last element using negative indexing
print("\nLast Fruit:")
print(fruits[-1])

# Creating a single-element tuple
single = (10,)

print("\nSingle Element Tuple:")
print(single)

print("Type:")
print(type(single))

# Difference between a tuple and a normal value
value = (10)

print("\nType of (10):")
print(type(value))

print("\nType of (10,):")
print(type(single))


# -----------------------------
# Key Points
# -----------------------------
# 1. A tuple is an ordered collection of elements.
# 2. Tuples are generally written using parentheses ().
# 3. Tuple elements can be accessed using indexing.
# 4. Indexing starts from 0, while negative indexing starts from -1.
# 5. Tuples can contain different types of data.
# 6. A single-element tuple must contain a comma.
# 7. (10) is an integer, whereas (10,) is a tuple.
# 8. Tuples are immutable, so their elements cannot be changed.
