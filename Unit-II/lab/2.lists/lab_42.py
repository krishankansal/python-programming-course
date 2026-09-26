# Lab 42: Searching and Filtering List Elements
# Objective:
# To learn how to search for elements in a list and filter elements
# based on a condition.

# 1. Searching for a student
students = ["Alice", "Bob", "Charlie", "David"]

name = input("Enter student name to search: ")

if name in students:
    print("Student Found")
else:
    print("Student Not Found")

# 2. Filtering even numbers
numbers = [10, 15, 22, 31, 40, 55, 62]

print("\nEven Numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)

# 3. Filtering passing marks
marks = [35, 78, 45, 28, 91, 67]

print("\nPassing Marks:")

for mark in marks:
    if mark >= 40:
        print(mark)

# Key Notes
# 1. The in operator can be used to search for an element.
# 2. A for loop can be used to examine every element.
# 3. An if condition can be used to filter elements.
# 4. Lists can be combined with loops and conditions for data processing.
# 5. Searching and filtering are important operations when working with real-world data.