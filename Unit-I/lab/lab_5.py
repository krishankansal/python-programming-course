# Lab 5: Arithmetic Operators in Python
# Objective : To learn how to perform mathematical calculations using Python's arithmetic operators and evaluate arithmetic expressions through simple programming examples.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nArithmetic Operations")
print("---------------------")

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)
print("Floor Division :", num1 // num2)
print("Modulus        :", num1 % num2)
print("Power          :", num1 ** num2)

# Key Notes
# 1. / always returns a float, even when the result is a whole number.
# 2. // returns the quotient without the decimal part.
# 3. % is commonly used to determine whether a number is even or odd.
# 4. ** is used to calculate powers and exponents.
# 5. Arithmetic operators work with both integers and floating-point numbers.