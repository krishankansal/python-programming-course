# Lab 46: List Comprehension
# Objective:
# To learn list comprehension and use it to create new lists
# from existing sequences.

# 1. Creating a list of squares
squares = [x ** 2 for x in range(1, 6)]

print("Squares:")
print(squares)

# 2. Creating a list of even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

print("\nEven Numbers:")
print(even_numbers)

# 3. Converting names to uppercase
names = ["alice", "bob", "charlie", "david"]

upper_names = [name.upper() for name in names]

print("\nNames in Uppercase:")
print(upper_names)

# 4. Filtering passing marks
marks = [35, 78, 45, 28, 91, 67]

passed = [mark for mark in marks if mark >= 40]

print("\nPassing Marks:")
print(passed)

# Key Notes
# 1. List comprehension provides a short way to create a new list.
# 2. The basic syntax is [expression for item in iterable].
# 3. A condition can be added using if.
# 4. List comprehension combines looping and list creation in one expression.
# 5. Students should first understand normal for loops before using list comprehension.