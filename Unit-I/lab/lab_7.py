# Lab 7: Logical Operators in Python
# Objective : To learn how to combine multiple conditions using Python's logical operators (and, or, and not) and understand how they evaluate Boolean expressions.

num = int(input("Enter a number: "))

print("\nLogical Operator Results")
print("------------------------")

print("num > 0 and num < 100 :", num > 0 and num < 100)
print("num < 0 or num > 100  :", num < 0 or num > 100)
print("not(num == 0)         :", not(num == 0))

# Key Notes
# 1. and requires all conditions to be True.
# 2. or requires at least one condition to be True.
# 3. not reverses the result of a Boolean expression.
# 4. Logical operators are mostly used with comparison operators.
# 5. They are essential for writing complex conditions in if, while, and other control statements.

