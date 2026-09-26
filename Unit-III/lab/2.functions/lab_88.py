# Lab No. 88: Local Variables in Nested Functions
#
# Objective:
# To understand the scope of variables in nested functions and how
# a variable defined inside an inner function is separate from one
# defined in the outer function.

# Program

def function1():  # outer function
    x = 2  # Variable defined within the outer function

    def function2(a):  # inner function
        # Define a new variable within the inner function
        # rather than changing the value of x of the outer function
        x = 6
        print(a + x)

    print(x)  # Display the value of x of the outer function
    function2(3)


function1()


# -----------------------------
# Key Points
# -----------------------------
# 1. function1() is the outer function.
# 2. function2() is nested inside function1().
# 3. x in function1() is a local variable of the outer function.
# 4. x in function2() is a separate local variable of the inner function.
# 5. The inner function uses its own x when calculating a + x.
# 6. Variables defined in different function scopes can have the same name.
