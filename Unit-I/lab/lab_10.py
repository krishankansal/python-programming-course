# Lab 10: Nested if Statement in Python
# Objective : To learn how to use nested if statements to test multiple conditions one inside another.

num = int(input("Enter a positive number: "))

print("\nResult")
print("------")

if num > 0:
    if num % 2 == 0:
        print("The number is Positive and Even.")
    else:
        print("The number is Positive and Odd.")
else:
    print("The number is not Positive.")

# Key Notes
# 1. A nested if statement is an if statement inside another if statement.
# 2. The inner if statement is executed only if the outer if condition is True.
# 3. Nested if statements are useful for checking multiple dependent conditions.
# 4. Proper indentation is essential in nested if statements.
# 5. Nested if statements improve decision-making in complex programs.