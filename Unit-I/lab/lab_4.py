# Lab 4: Taking Input from the User
# Objective : To learn how to accept input from the user using Python's input() function, store the entered data in variables, and convert the input into the required data type using type casting.

# Syntax

# variable_name = input("Prompt Message")

# Input String
name = input("Enter your name: ")

# Input Integer
age = int(input("Enter your age: "))

# Input Float
percentage = float(input("Enter your percentage: "))

# Display Output
print("\n----- Student Details -----")
print("Name       :", name)
print("Age        :", age)
print("Percentage :", percentage)

# Display Data Types
print("\nData Types")
print(type(name))
print(type(age))
print(type(percentage))

# Key Notes
# 1. input() is used to accept user input.
# 2. The value returned by input() is always of type str.
# 3. Use int() to convert input into an integer.
# 4. Use float() to convert input into a floating-point number.
# 5. A meaningful prompt message improves user experience.
# 6. If the entered value cannot be converted into the required type, Python raises a ValueError