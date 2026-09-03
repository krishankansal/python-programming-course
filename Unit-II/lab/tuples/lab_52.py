# Lab 52: Introduction to Tuples
# Objective:
# To understand tuples, create tuples and access their elements
# using indexing.


# 1. Creating a tuple

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits Tuple:")
print(fruits)


# 2. Creating a tuple of numbers

numbers = (10, 20, 30, 40, 50)

print("\nNumbers Tuple:")
print(numbers)


# 3. Creating a tuple with different data types

student = ("Rahul", 21, 85.5, True)

print("\nStudent Tuple:")
print(student)


# 4. Checking the type of a tuple

print("\nType of student:")
print(type(student))


# 5. Accessing the first element

print("\nFirst Fruit:")
print(fruits[0])


# 6. Accessing the third element

print("\nThird Fruit:")
print(fruits[2])


# 7. Accessing the last element using negative indexing

print("\nLast Fruit:")
print(fruits[-1])


# 8. Creating a single-element tuple

single = (10,)

print("\nSingle Element Tuple:")
print(single)

print("Type:")
print(type(single))


# 9. Difference between a tuple and a normal value

value = (10)

print("\nType of (10):")
print(type(value))

print("\nType of (10,):")
print(type(single))


# Key Notes
# 1. A tuple is an ordered collection of elements.
# 2. Tuples are generally written using parentheses ().
# 3. Tuple elements can be accessed using indexing.
# 4. Indexing starts from 0.
# 5. Negative indexing starts from -1.
# 6. Tuples can contain different types of data.
# 7. A single-element tuple must contain a comma.
# 8. (10) is an integer, whereas (10,) is a tuple.
# 9. Tuples are immutable, which means their elements cannot
#    be changed after the tuple is created.