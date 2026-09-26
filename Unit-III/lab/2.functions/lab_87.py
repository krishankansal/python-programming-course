# Lab No. 87: Nested Function with Arguments
#
# Objective:
# To understand how arguments can be passed from an outer function
# to a nested inner function.

# Program

def funct1(x, y):

    def funct2(x, y):
        print('Multiplication =', x * y)

    funct2(x, y)


funct1(10, 20)


# -----------------------------
# Key Points
# -----------------------------
# 1. funct1() is the outer function.
# 2. funct2() is a nested function defined inside funct1().
# 3. The outer function receives x and y as arguments.
# 4. The values are passed to the inner function.
# 5. funct2() performs the multiplication and displays the result.
