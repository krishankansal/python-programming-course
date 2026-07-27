# Lab 18: Check Prime Number using Nested Loop
# Objective : To learn how to check whether a number is prime using a loop and conditional statements.

num = int(input("Enter a positive integer: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print("\nResult")
print("------")

if is_prime:
    print(num, "is a Prime Number.")
else:
    print(num, "is Not a Prime Number.")

# Key Notes
# 1. A prime number has exactly two factors: 1 and itself.
# 2. The for loop checks divisibility from 2 to num - 1.
# 3. The modulus (%) operator is used to test divisibility.
# 4. The break statement exits the loop as soon as a factor is found.
# 5. Using break improves the efficiency of the program by avoiding unnecessary iterations.