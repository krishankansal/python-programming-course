# Lab No. 68: Python Functions and return None
#
# Objective:
# To understand how to define and call a function and how a function
# returns the special value None.

# Program

def my_function():
    print("Hello from a function")
    return None


x = my_function()
print(x)


# -----------------------------
# Key Points
# -----------------------------
# 1. def is used to define a function in Python.
# 2. A function is executed when it is called.
# 3. The return statement is used to return a value from a function.
# 4. None represents the absence of a value.
# 5. x = my_function() stores the returned value in x.
# 6. If a function has no return statement, Python automatically returns None.
