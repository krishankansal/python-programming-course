# Lab No. 56: Combining filter() and map()
#
# Objective:
# To calculate the squares of even numbers using filter() and map(),
# lambda functions, and list comprehension.

# Program

# Using user-defined functions
def square(x):
    return x * x


def iseven(x):
    return x % 2 == 0


lst = list(map(square, filter(iseven, range(20))))
print(lst)

# Using lambda functions
lst = list(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, range(20)))
)
print(lst)

# Using list comprehension
lst = [x * x for x in range(20) if x % 2 == 0]
print(lst)


# -----------------------------
# Key Points
# -----------------------------
# 1. filter() is used to select even numbers.
# 2. map() is used to calculate the square of each selected number.
# 3. User-defined functions can be used with filter() and map().
# 4. lambda functions provide concise operations.
# 5. List comprehension provides another concise solution.
