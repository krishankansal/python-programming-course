# Lab 36: List Slicing in Python
# Objective:
# To learn how to extract a portion of a list using slicing.

# 1. Creating a list
marks = [78, 85, 92, 67, 88, 74]

print("Original List:")
print(marks)

# 2. Accessing elements from index 1 to 3
print("\nElements from index 1 to 3:")
print(marks[1:4])

# 3. Accessing the first three elements
print("\nFirst Three Elements:")
print(marks[:3])

# 4. Accessing elements from index 3 to the end
print("\nElements from index 3 to the end:")
print(marks[3:])

# 5. Accessing alternate elements
print("\nAlternate Elements:")
print(marks[::2])

# 6. Reversing a list using slicing
print("\nList in Reverse Order:")
print(marks[::-1])

# Key Notes
# 1. List slicing is used to extract a portion of a list.
# 2. The syntax is list[start:stop:step].
# 3. The start index is included.
# 4. The stop index is excluded.
# 5. If start or stop is omitted, Python uses the beginning or end of the list.
# 6. A step of 2 selects alternate elements.
# 7. A step of -1 reverses the list.