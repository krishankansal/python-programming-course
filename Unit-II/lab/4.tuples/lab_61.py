# Lab No. 61: Working with Tuples
#
# Objective:
# To understand tuple immutability, tuple packing, unpacking,
# swapping variables and converting between lists and tuples.

# Program

# Tuple Packing
student = "Rahul", 21, "BCA"

print("Packed Tuple:")
print(student)

# Tuple Unpacking
name, age, course = student

print("\nName:")
print(name)

print("Age:")
print(age)

print("Course:")
print(course)

# Unpacking a Tuple using Multiple Variables
marks = (78, 85, 92)

maths, science, computer = marks

print("\nMarks:")
print("Maths:", maths)
print("Science:", science)
print("Computer:", computer)

# Swapping Two Variables using Tuple Unpacking
a = 10
b = 20

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)

# Demonstrating Tuple Immutability
numbers = (10, 20, 30)

print("\nOriginal Tuple:")
print(numbers)

# Tuples are immutable.
# Therefore, the following statement will generate an error.
# numbers[0] = 100

# Creating a New Tuple
numbers = (10, 20, 30)

new_numbers = (100,) + numbers[1:]

print("\nOriginal Tuple:")
print(numbers)

print("\nNew Tuple:")
print(new_numbers)

# Nested Tuple
college = (
    "ABC College",
    ("BCA", "BBA", "B.Tech"),
    2026
)

print("\nCollege Information:")
print(college)

print("\nCollege Name:")
print(college[0])

print("\nCourses:")
print(college[1])

print("\nFirst Course:")
print(college[1][0])

# Converting a List into a Tuple
marks_list = [75, 82, 91, 68]

marks_tuple = tuple(marks_list)

print("\nOriginal List:")
print(marks_list)

print("\nConverted Tuple:")
print(marks_tuple)

# Converting a Tuple into a List
marks_list_again = list(marks_tuple)

print("\nTuple Converted Back to List:")
print(marks_list_again)

# Using Tuple Unpacking with a Function
def get_student():
    return "Aman", 21, "BCA"


student_name, student_age, student_course = get_student()

print("\nStudent Information:")
print("Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)


# -----------------------------
# Key Points
# -----------------------------
# 1. Tuple packing means putting multiple values into one tuple.
# 2. Tuple unpacking means assigning tuple elements to variables.
# 3. The number of variables should normally match the number of elements.
# 4. Tuples are immutable.
# 5. Individual tuple elements cannot be changed after creation.
# 6. Tuple unpacking can be used to swap variables.
# 7. A tuple can contain another tuple.
# 8. tuple() converts a list into a tuple.
# 9. list() converts a tuple into a list.
# 10. A function can return multiple values as a tuple.
