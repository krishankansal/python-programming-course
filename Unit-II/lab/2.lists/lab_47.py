# Lab 47: Student Marks Analysis Using Lists
# Objective:
# To apply list concepts, loops, conditions, and built-in functions
# to perform a simple student marks analysis.

# 1. Creating student and marks lists
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
marks = [78, 92, 35, 67, 88]

# 2. Displaying student-wise marks
print("Student Performance:")

for i in range(len(students)):
    print(students[i], ":", marks[i])

# 3. Calculating total marks
total = sum(marks)

print("\nTotal Marks:")
print(total)

# 4. Calculating average marks
average = sum(marks) / len(marks)

print("\nAverage Marks:")
print(average)

# 5. Finding highest marks
print("\nHighest Marks:")
print(max(marks))

# 6. Finding lowest marks
print("\nLowest Marks:")
print(min(marks))

# 7. Displaying passed students
print("\nPassed Students:")

for i in range(len(students)):
    if marks[i] >= 40:
        print(students[i])

# Key Notes
# 1. Multiple lists can be used together to represent related data.
# 2. The same index can be used to connect a student with their marks.
# 3. len(), sum(), max(), and min() are useful for marks analysis.
# 4. Loops and conditions can be combined with lists for data processing.
# 5. This type of list processing provides a foundation for working with tabular data.