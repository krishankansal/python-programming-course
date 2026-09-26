# Lab No. 76: Function with *args (Variable Arguments)
#
# Objective:
# To understand how *args allows a function to accept a variable
# number of positional arguments.

# Program

def calculate_total(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total


print(calculate_total(1, 2, 3))
print(calculate_total(10, 20, 30, 40))


# -----------------------------
# Key Points
# -----------------------------
# 1. *args allows a function to accept a variable number of arguments.
# 2. Inside the function, numbers is treated as a tuple of arguments.
# 3. The for loop processes each supplied number.
# 4. total accumulates the sum of all arguments.
# 5. The same function can be called with different numbers of arguments.
