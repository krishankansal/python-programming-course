# LAB 61: Python Functions and `return None`

## Objective of the Program

# To understand how to define and call a function in Python and how a function returns the special value `None`.

## Lab
# A function is a reusable block of code that performs a specific task. In Python, 
# a function is defined using the `def` keyword. A function can return a value 
# using the `return` statement. If a function does not return any value, Python 
# returns `None` by default.

## Program

def my_function():

    print("Hello from a function")
    return  None

x = my_function()
print(x)

## Output

# Hello from a function
# None

## Key Points

# 1. `def` is used to define a function in Python.
# 2. A function is executed when it is called.
# 3. `my_function()` calls the function.
# 4. The `return` statement is used to return a value from a function.
# 5. `None` represents the absence of a value.
# 6. `x = my_function()` stores the returned value of the function in `x`.
# 7. If a function has no `return` statement, Python automatically returns `None`.
# 8. `print(x)` therefore displays `None`.


