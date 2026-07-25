# Lab 2: The print() Function
# Objective : To learn how to use Python's print() function to display text, numbers, variables, and expressions, and to format the output using the sep and end keyword arguments along with common escape sequences.

# Basic Syntax
# print(*objects, sep=' ', end='\n')

# *objects → values to display.
# sep → separator between multiple values.
# end → what is printed at the end of the output.

# Printing a Single Value
print("Hello Python")

# Printing Multiple Values
name = "Rox"
age = 20
print(name, age)

# The sep Keyword Argument
print("Python", "Java", "C++")
print("Python", "Java", "C++", sep="-")
print("Python", "Java", "C++", sep=" |")

# The end Keyword Argument
print("Hello", end=" ")
print("Python")

# Combining sep and end?
print(10, 20, 30, sep=" : ", end=" <- End")

# Escape Sequences
print("Line1\nLine2")
print("A\tB\tC")
print("C:\\Python")
print("\"Hello\"")

