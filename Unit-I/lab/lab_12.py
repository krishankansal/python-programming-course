# Lab 12: The range() Function in Python
# Objective : To learn how to use the range() function to generate a sequence of numbers.

print("range(5)")
print("--------")
for i in range(5):
    print(i)

print("\nrange(2, 8)")
print("-----------")
for i in range(2, 8):
    print(i)

print("\nrange(1, 11, 2)")
print("----------------")
for i in range(1, 11, 2):
    print(i)


# Key Notes
# 1. range() generates a sequence of numbers.
# 2. range(stop) generates numbers from 0 to stop - 1.
# 3. range(start, stop) generates numbers from start to stop - 1.
# 4. range(start, stop, step) generates numbers with the specified step size.
# 5. The range() function is commonly used with the for loop.