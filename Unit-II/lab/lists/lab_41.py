# Lab 41: Traversing a List Using a for Loop
# Objective:
# To learn how to access and process each element of a list
# using a for loop.

# 1. Creating a list
students = ["Alice", "Bob", "Charlie", "David"]

# 2. Displaying each student
print("Student Names:")

for student in students:
    print(student)

# 3. Displaying marks
marks = [78, 85, 92, 67, 88]

print("\nStudent Marks:")

for mark in marks:
    print(mark)

# 4. Calculating the total using a loop
total = 0

for mark in marks:
    total = total + mark

print("\nTotal Marks:")
print(total)

# 5. Calculating the average
average = total / len(marks)

print("\nAverage Marks:")
print(average)

# Key Notes
# 1. A for loop can be used to traverse each element of a list.
# 2. The loop variable represents one element at a time.
# 3. Lists can be processed using loops for calculations and analysis.
# 4. len() returns the number of elements in a list.
# 5. A loop can be used to calculate total, average, count, and other values.