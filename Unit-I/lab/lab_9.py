# Lab 9: Decision Making using if-else in Python
# Objective : To learn how to make decisions in Python using if, if-else, and if-elif-else statements.

marks = int(input("Enter your marks (0-100): "))

print("\nResult")
print("------")

if marks >= 90:
    print("Grade : A")
elif marks >= 75:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >= 40:
    print("Grade : D")
else:
    print("Grade : Fail")

# Key Notes
# 1. if is used to test a condition.
# 2. else executes when the if condition is False.
# 3. elif is used to check multiple conditions.
# 4. Only one block of an if-elif-else statement is executed.
# 5. Indentation is mandatory in Python decision-making statements.