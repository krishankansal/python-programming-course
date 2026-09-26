# Lab No. 57: Nested List Comprehension
#
# Objective:
# To create a multiplication table using nested list comprehension
# and understand how nested comprehensions generate two-dimensional data.

# Program

# Creating a multiplication table as a list of lists
multiplication_table = [
    [i * j for j in range(1, 5)]
    for i in range(1, 6)
]
print(multiplication_table)

# Creating a multiplication table as a list of tuples
multiplication_table = [
    tuple(i * j for j in range(1, 5))
    for i in range(1, 6)
]
print(multiplication_table)

# Using a list comprehension inside tuple()
multiplication_table = [
    tuple([i * j for j in range(1, 5)])
    for i in range(1, 6)
]
print(multiplication_table)


# -----------------------------
# Key Points
# -----------------------------
# 1. A nested list comprehension contains one comprehension inside another.
# 2. The outer comprehension controls the rows.
# 3. The inner comprehension generates values within each row.
# 4. tuple() can convert generated values into tuples.
# 5. Nested comprehensions are useful for two-dimensional data.
