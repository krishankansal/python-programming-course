# Lab 14: Multiplication Table using for Loop
# Objective : To learn how to use the for loop to generate the multiplication table of a given number.

num = int(input("Enter a number: "))

print("\nMultiplication Table")
print("--------------------")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Key Notes
# 1. The for loop repeats a block of code for each value in a sequence.
# 2. range(1, 11) generates numbers from 1 to 10.
# 3. The loop variable i represents the current multiplier.
# 4. Each iteration calculates and displays one row of the multiplication table.
# 5. The for loop is ideal when the number of iterations is known.