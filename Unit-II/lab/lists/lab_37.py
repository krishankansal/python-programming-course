# Lab 37: Basic List Operations in Python
# Objective:
# To learn basic operations on lists such as concatenation,
# repetition, membership, and comparison.

# 1. List Concatenation using + operator
list1 = [10, 20, 30]
list2 = [40, 50, 60]

print("List Concatenation:")
print(list1 + list2)

# 2. List Repetition using * operator
print("\nList Repetition:")
print([1, 2, 3] * 3)

# 3. Membership using in operator
students = ["Alice", "Bob", "Charlie"]

print("\nMembership Checking:")
print("Bob" in students)
print("David" in students)

# 4. Non-membership using not in operator
print("\nNon-Membership Checking:")
print("David" not in students)

# 5. Comparing two lists
numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30]

print("\nList Comparison:")
print(numbers1 == numbers2)

# Key Notes
# 1. The + operator joins two or more lists.
# 2. The * operator repeats the elements of a list.
# 3. The in operator checks whether an element exists in a list.
# 4. The not in operator checks whether an element does not exist in a list.
# 5. The == operator checks whether two lists contain the same elements in the same order.
# 6. List operations generally create a new list rather than modifying the original list.