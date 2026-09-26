# Lab 33: String Formatting in Python
# Objective:
# To learn how to format strings using the format() method and f-strings.

# -----------------------------------------
# 1. Using format() Method
# -----------------------------------------

name = "Aman"
course = "BCA"
marks = 89

print("Using format() Method:")
print("Name: {}".format(name))
print("Course: {}".format(course))
print("Marks: {}".format(marks))

# -----------------------------------------
# 2. Multiple Placeholders
# -----------------------------------------

print("\nMultiple Placeholders:")
print("Student {} studies {} and scored {} marks.".format(name, course, marks))

# -----------------------------------------
# 3. Positional Formatting
# -----------------------------------------

print("\nPositional Formatting:")
print("{0} is studying {1}.".format(name, course))
print("{1} student is {0}.".format(name, course))

# -----------------------------------------
# 4. Using f-Strings
# -----------------------------------------

print("\nUsing f-Strings:")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Marks: {marks}")

# -----------------------------------------
# 5. Expressions in f-Strings
# -----------------------------------------

a = 15
b = 25

print("\nExpressions in f-Strings:")
print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")

# -----------------------------------------
# 6. Practical Example
# -----------------------------------------

student = "Riya"
subject = "Python"
percentage = 91.5

print("\nStudent Report:")
print(f"{student} scored {percentage}% in {subject}.")

# -----------------------------------------
# Key Notes
# -----------------------------------------

# 1. String formatting is used to insert values into a string.
# 2. The format() method replaces {} placeholders with specified values.
# 3. Placeholders can be numbered using {0}, {1}, etc.
# 4. An f-string is created by placing the letter f before the opening quotation mark.
# 5. Variables and expressions can be placed directly inside {} in an f-string.
# 6. f-strings are easier to read and are generally faster than the format() method.
# 7. Both format() and f-strings return new strings without modifying the original string.