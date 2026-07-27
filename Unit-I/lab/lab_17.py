# Lab 17: Reverse a Number using a while Loop
# Objective : To learn how to reverse the digits of a number using a while loop and arithmetic operators.

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("\nResult")
print("------")
print("Original Number :", original)
print("Reversed Number :", reverse)

# Key Notes
# 1. The while loop executes as long as the given condition is True.
# 2. The modulus (%) operator extracts the last digit of a number.
# 3. The floor division (//) operator removes the last digit.
# 4. The reversed number is built one digit at a time.
# 5. Reversing a number is useful in problems such as palindrome checking and digit manipulation.