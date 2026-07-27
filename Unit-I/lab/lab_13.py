# Lab 13: Sum of First N Natural Numbers using for Loop
# Objective : To learn how to use the for loop to perform repetitive calculations.

n = int(input("Enter a positive integer: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("\nResult")
print("------")
print("Sum of first", n, "natural numbers =", sum)

# Key Notes
# 1. A for loop executes a block of code repeatedly.
# 2. range(1, n + 1) generates numbers from 1 to n.
# 3. The loop variable changes automatically in each iteration.
# 4. Variables can be updated inside the loop to accumulate results.
# 5. The for loop is suitable when the number of iterations is known.