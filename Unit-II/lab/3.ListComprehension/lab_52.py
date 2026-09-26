# Lab No. 52: Multiple Conditions in List Comprehension
#
# Objective:
# To understand the use of multiple conditions and the logical OR
# operator in list comprehension.

# Program

# Numbers divisible by both 2 and 5
num_list = [y for y in range(101) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# Numbers divisible by either 2 or 5
num_list = [y for y in range(100) if y % 2 == 0 or y % 5 == 0]
print(num_list)


# -----------------------------
# Key Points
# -----------------------------
# 1. Multiple if conditions can be used in list comprehension.
# 2. Multiple if conditions work like an AND condition.
# 3. The OR operator selects an item when either condition is true.
# 4. The modulo operator (%) is used to test divisibility.
