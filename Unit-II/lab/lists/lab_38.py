# Lab 38: Modifying Elements of a List
# Objective:
# To understand that lists are mutable and learn how to modify
# existing elements of a list.

# 1. Creating a list
students = ["Alice", "Bob", "Charlie", "David"]

print("Original List:")
print(students)

# 2. Changing the first element
students[0] = "Emma"

print("\nAfter Changing First Element:")
print(students)

# 3. Changing the third element
students[2] = "Frank"

print("\nAfter Changing Third Element:")
print(students)

# 4. Modifying multiple elements using slicing
students[1:3] = ["George", "Helen"]

print("\nAfter Modifying Multiple Elements:")
print(students)

# Key Notes
# 1. Lists are mutable.
# 2. An existing list element can be changed using its index.
# 3. Multiple elements can be changed using slicing.
# 4. The original list is modified when an element is assigned a new value.
# 5. This is an important difference between lists and strings.