# Lab 3: Type Casting (Type Conversion)
# Objective : To learn how to convert data from one data type to another using Python's built-in type conversion functions such as int(), float(), str(), and bool(), and to understand the need for type casting in Python programs.

num = 25
print("Original Value :", num)
print("Original Type  :", type(num))

num_float = float(num)
print("Converted Value:", num_float)
print("Converted Type :", type(num_float))

print()

# Float to Integer
marks = 89.75
print("Original Value :", marks)
print("Original Type  :", type(marks))

marks_int = int(marks)
print("Converted Value:", marks_int)
print("Converted Type :", type(marks_int))

print()

# Integer to String
age = 20
age_str = str(age)

print(age_str)
print(type(age_str))

print()

# String to Integer
number = "100"
number_int = int(number)

print(number_int)
print(type(number_int))

print()

# Integer to Boolean
print(bool(0))
print(bool(25))

print()

# String to Boolean
print(bool(""))
print(bool("Python"))

# Key Notes
# 1. Type casting is the process of converting one data type into another.
# 2. Python supports explicit type conversion using built-in functions.
# 3. int() removes the decimal portion; it does not round the value.
# 4. float() always produces a decimal number.
# 5. str() converts numbers into text.
# 6. bool(0) and bool("") return False.
# 7. Most non-zero numbers and non-empty strings evaluate to True.