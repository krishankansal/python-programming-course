# Lab 45: Working with Nested Lists
# Objective:
# To understand nested lists and learn how to access elements
# from lists containing other lists.

# 1. Creating a nested list
students = [
    ["Alice", 20, 8.5],
    ["Bob", 21, 7.8],
    ["Charlie", 20, 9.1]
]

print("Student Data:")
print(students)

# 2. Accessing the first student's name
print("\nFirst Student Name:")
print(students[0][0])

# 3. Accessing the second student's CGPA
print("\nSecond Student CGPA:")
print(students[1][2])

# 4. Displaying each student record
print("\nStudent Records:")

for student in students:
    print(student)

# 5. Displaying student names only
print("\nStudent Names:")

for student in students:
    print(student[0])

# Key Notes
# 1. A list can contain other lists. Such a structure is called a nested list.
# 2. The first index identifies the inner list.
# 3. The second index identifies an element inside that inner list.
# 4. students[1][2] means the third element of the second inner list.
# 5. Nested lists are useful for representing tabular data.