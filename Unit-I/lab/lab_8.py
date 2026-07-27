# Lab 8: The if Statement in Python

# Objective:
# To learn how to use the if statement to execute a block of code only when a specified condition is True.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

print("Program Finished")

#----------------------------------------------

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Result : PASS")

print("End of Program")

#----------------------------------------------
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")

print("Execution Completed")

#----------------------------------------------
temperature = float(input("Enter temperature in °C: "))

if temperature >= 40:
    print("Heat Wave Alert")

print("Stay Safe")

"""
# Key Notes
# 1. The if statement checks whether a condition is True.
# 2. The indented block executes only if the condition is True.
# 3. If the condition is False, the if block is skipped.
# 4. Indentation is mandatory in Python.
# 5. The program continues executing after the if block.

Practice Questions
------------------

Write Python programs to:

Check whether a number is positive.
Check whether a number is divisible by 5.
Check whether a student has scored above 90 marks.
Check whether a person is a senior citizen (age ≥ 60).
"""