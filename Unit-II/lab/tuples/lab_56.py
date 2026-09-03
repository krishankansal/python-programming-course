# Lab 56: Tuple Functions and Methods
# Objective:
# To learn commonly used built-in functions and methods
# used with tuples.


# 1. Creating a tuple

numbers = (10, 20, 30, 20, 40, 20, 50)

print("Numbers Tuple:")
print(numbers)


# 2. len() Function

print("\nLength of Tuple:")
print(len(numbers))


# 3. max() Function

print("\nMaximum Value:")
print(max(numbers))


# 4. min() Function

print("\nMinimum Value:")
print(min(numbers))


# 5. sum() Function

print("\nSum of Values:")
print(sum(numbers))


# 6. count() Method

print("\nNumber of times 20 occurs:")
print(numbers.count(20))

print("\nNumber of times 30 occurs:")
print(numbers.count(30))


# 7. index() Method

print("\nIndex of 40:")
print(numbers.index(40))

print("\nIndex of 50:")
print(numbers.index(50))


# 8. Using Functions with a Tuple of Marks

marks = (78, 85, 92, 67, 88)

print("\nMarks:")
print(marks)

print("\nNumber of Students:")
print(len(marks))

print("Highest Marks:")
print(max(marks))

print("Lowest Marks:")
print(min(marks))

print("Total Marks:")
print(sum(marks))

print("Average Marks:")
print(sum(marks) / len(marks))


# 9. Counting Repeated Values

attendance = (90, 85, 90, 75, 90, 80)

print("\nAttendance:")
print(attendance)

print("Number of students with 90% attendance:")
print(attendance.count(90))


# 10. Finding the Position of an Element

subjects = ("Python", "DBMS", "Java", "Python", "AI")

print("\nSubjects:")
print(subjects)

print("\nFirst occurrence of Python:")
print(subjects.index("Python"))

print("\nNumber of times Python occurs:")
print(subjects.count("Python"))


# 11. Combining Functions and Methods

numbers = (5, 10, 15, 20, 10, 25, 10)

print("\nNumbers:")
print(numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Number of 10s:", numbers.count(10))
print("First position of 10:", numbers.index(10))


# Key Notes
# 1. len() returns the number of elements in a tuple.
# 2. max() returns the largest value.
# 3. min() returns the smallest value.
# 4. sum() returns the sum of numeric elements.
# 5. count() is a tuple method used to count occurrences
#    of a particular element.
# 6. index() is a tuple method used to find the position
#    of the first occurrence of an element.
# 7. Tuples have two important built-in methods:
#    count() and index().
# 8. Built-in functions such as len(), max(), min()
#    and sum() can also be used with tuples.
# 9. index() returns the position of the first occurrence
#    when an element appears multiple times.