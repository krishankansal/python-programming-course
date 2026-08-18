# Lab 35: Accessing Elements of a List
# Objective:
# To learn how to access individual elements of a list using
# positive and negative indexing.

# 1. Creating a list
students = ["Alice", "Bob", "Charlie", "David", "Eva"]

print("Students:")
print(students)

# 2. Accessing the first element
print("\nFirst Student:")
print(students[0])

# 3. Accessing the third element
print("\nThird Student:")
print(students[2])

# 4. Accessing the last element using positive indexing
print("\nLast Student:")
print(students[4])

# 5. Accessing the last element using negative indexing
print("\nLast Student using Negative Index:")
print(students[-1])

# 6. Accessing the second-last element
print("\nSecond-Last Student:")
print(students[-2])

# Key Notes
# 1. List indexing starts from 0.
# 2. The first element is accessed using index 0.
# 3. Negative indexing starts from -1.
# 4. -1 represents the last element of the list.
# 5. -2 represents the second-last element.
# 6. Accessing an invalid index produces an IndexError.