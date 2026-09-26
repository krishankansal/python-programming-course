# Lab 39: Adding Elements to a List
# Objective:
# To learn different ways of adding elements to a list using
# append(), insert(), and extend() methods.

# 1. Adding an element using append()
students = ["Alice", "Bob", "Charlie"]

students.append("David")

print("After append():")
print(students)

# 2. Adding an element at a specific position using insert()
students.insert(1, "Emma")

print("\nAfter insert():")
print(students)

# 3. Adding multiple elements using extend()
students.extend(["Frank", "George"])

print("\nAfter extend():")
print(students)

# 4. Comparing append() and extend()
numbers = [10, 20]

numbers.append([30, 40])

print("\nAfter append([30, 40]):")
print(numbers)

numbers = [10, 20]

numbers.extend([30, 40])

print("\nAfter extend([30, 40]):")
print(numbers)

# Key Notes
# 1. append() adds one element at the end of a list.
# 2. insert() adds an element at a specified position.
# 3. extend() adds multiple elements to the end of a list.
# 4. append([30, 40]) adds the entire list as one element.
# 5. extend([30, 40]) adds 30 and 40 as separate elements.