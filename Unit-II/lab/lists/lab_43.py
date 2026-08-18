# Lab 43: Built-in Functions with Lists
# Objective:
# To learn and use important Python built-in functions with lists.

# 1. Creating a list of marks
marks = [78, 85, 92, 67, 88]

# 2. Finding the number of elements using len()
print("Number of Students:")
print(len(marks))

# 3. Finding the total using sum()
print("\nTotal Marks:")
print(sum(marks))

# 4. Finding the minimum value using min()
print("\nLowest Marks:")
print(min(marks))

# 5. Finding the maximum value using max()
print("\nHighest Marks:")
print(max(marks))

# 6. Sorting using sorted()
print("\nSorted Marks:")
print(sorted(marks))

# 7. Calculating the average
print("\nAverage Marks:")
print(sum(marks) / len(marks))

# Key Notes
# 1. len() returns the number of elements in a list.
# 2. sum() returns the total of numerical elements.
# 3. min() returns the smallest element.
# 4. max() returns the largest element.
# 5. sorted() returns a new sorted list.
# 6. sorted() does not change the original list.