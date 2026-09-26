# Lab 15: Factorial of a Number using for Loop
# Objective : To learn how to calculate the factorial of a number using a for loop.

num = int(input("Enter a non-negative integer: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("\nResult")
print("------")
print("Factorial of", num, "=", factorial)

# Key Notes
# 1. The factorial of a number n is the product of all integers from 1 to n.
# 2. 0! is defined as 1.
# 3. A variable (factorial) is used to accumulate the product in each iteration.
# 4. The for loop repeats the multiplication until the last value in the range.
# 5. Factorials are widely used in mathematics, probability, and combinatorics.