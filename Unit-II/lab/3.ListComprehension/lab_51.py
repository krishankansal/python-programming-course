# Lab No. 51: List Comprehension with if Condition
#
# Objective:
# To create a list of squares of even numbers using a for loop,
# list comprehension, and filter() with map().

# Program

# Using a traditional for loop
even_squares = []

for x in range(1, 21):
    if x % 2 == 0:
        even_squares.append(x ** 2)

print(even_squares)

# Using list comprehension
number_list = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(number_list)

# Using filter() and map() with lambda functions
number_list = list(
    map(lambda z: z ** 2,
        filter(lambda y: y % 2 == 0, range(1, 21)))
)
print(number_list)


# -----------------------------
# Key Points
# -----------------------------
# 1. An if condition can be included in list comprehension.
# 2. The modulo operator (%) is used to check whether a number is even.
# 3. filter() selects elements that satisfy a condition.
# 4. map() applies an operation to the filtered elements.
# 5. Different approaches can solve the same problem.
