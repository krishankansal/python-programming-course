# Lab No. 49: Introduction to List Comprehension
#
# Objective:
# To understand list comprehension and compare it with the traditional
# for loop method for creating lists.

# Program

lst = []

for x in range(1, 11):
    lst.append(x)

print(lst)

# List of numbers from 1 to 10
lst = [x for x in range(1, 11)]
print(lst)

# Creating a list of squares using a traditional for loop
squares = []

for i in range(10):
    squares.append(i * i)

# Creating the same list using list comprehension
squares = [i * i for i in range(10)]
print(squares)


# -----------------------------
# Key Points
# -----------------------------
# 1. List comprehension provides a concise way to create a list.
# 2. The basic syntax is [expression for item in iterable].
# 3. A traditional for loop can be replaced by list comprehension.
# 4. List comprehension can create calculated values such as squares.
