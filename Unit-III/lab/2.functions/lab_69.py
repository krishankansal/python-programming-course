# LAB 62: Passing Arguments to a Function

## Objective of the Program

# To understand how to pass arguments to a function in Python using parameters.

## Lab

# A function can accept values through **parameters**. 
# The actual values passed to the function while calling it are called **arguments**.

## Program

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Shyam")  # "Shyam" is an argument

## Output
# Hello, Shyam!

## Key Points
# 1. A **parameter** is a variable defined in the function definition.
# 2. An **argument** is the actual value passed to a function.
# 3. `name` is the parameter.
# 4. `"Shyam"` is the argument.
# 5. The argument `"Shyam"` is assigned to the parameter `name`.
# 6. `f"Hello, {name}!"` is an **f-string** used to insert the value of `name` into 
# the string.
# 7. Comments beginning with `#` are used to explain the code and 
# are ignored by Python.

