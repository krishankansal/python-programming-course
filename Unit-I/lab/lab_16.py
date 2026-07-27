# Lab 16: Count Even and Odd Numbers from 1 to N
# Objective : To learn how to use a for loop with if-else to count even and odd numbers.

n = int(input("Enter a positive integer: "))

even_count = 0
odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("\nResult")
print("------")
print("Even Numbers :", even_count)
print("Odd Numbers  :", odd_count)

# Key Notes
# 1. A for loop is used to iterate through numbers from 1 to n.
# 2. The if-else statement checks whether a number is even or odd.
# 3. The modulus (%) operator returns the remainder after division.
# 4. Even and odd counters are updated during each iteration.
# 5. Combining loops with decision-making helps solve practical programming problems.