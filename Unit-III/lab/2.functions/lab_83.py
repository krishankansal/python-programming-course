# Lab No. 83: Assigning a Function to a Variable and Calling It
#
# Objective:
# To understand that a function can be assigned to a variable and
# then called through that variable.

# Program

def add_numbers(x, y):
    return x + y


x = add_numbers

print(x(10, 20))
print(type(x))


# -----------------------------
# Key Points
# -----------------------------
# 1. add_numbers is assigned to the variable x.
# 2. x and add_numbers refer to the same function object.
# 3. x(10, 20) calls the function through x.
# 4. The function returns the sum of the two arguments.
# 5. type(x) shows that x refers to a function object.
