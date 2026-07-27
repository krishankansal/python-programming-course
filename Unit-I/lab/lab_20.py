# Lab 20: Prime Factors of a Number
# Objective : To learn how to find the prime factors of a number using a while loop.

num = int(input("Enter a positive integer: "))

factor = 2

print("\nPrime Factors")
print("-------------")

while num > 1:
    if num % factor == 0:
        print(factor)
        num = num // factor
    else:
        factor = factor + 1

# Key Notes
# 1. A prime factor is a prime number that divides a given number exactly.
# 2. The algorithm starts checking from the smallest prime number (2).
# 3. If a factor divides the number, it is printed and removed using floor division (//).
# 4. The same factor is checked repeatedly until it no longer divides the number.
# 5. The process continues until the number becomes 1.