# Lab 29: String Methods-I in Python
# Objective:
# To learn commonly used string case conversion methods in Python.

text = "python programming"

print("Original String:")
print(text)

# 1. upper() Method
print("\nupper() Method:")
print(text.upper())

# 2. lower() Method
text1 = "PYTHON PROGRAMMING"

print("\nlower() Method:")
print(text1.lower())

# 3. title() Method
print("\ntitle() Method:")
print(text.title())

# 4. capitalize() Method
print("\ncapitalize() Method:")
print(text.capitalize())

# 5. swapcase() Method
text2 = "Python Programming"

print("\nswapcase() Method:")
print(text2.swapcase())

# Key Notes
# 1. upper() converts all characters of a string to uppercase.
# 2. lower() converts all characters of a string to lowercase.
# 3. title() converts the first letter of every word to uppercase.
# 4. capitalize() converts only the first letter of the entire string to uppercase and the remaining letters to lowercase.
# 5. swapcase() converts uppercase letters to lowercase and lowercase letters to uppercase.
# 6. These methods return a new string and do not modify the original string.
# 7. Since strings are immutable, the original string remains unchanged after calling these methods.