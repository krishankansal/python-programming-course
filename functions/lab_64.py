# LAB 64: Function with Multiple Parameters and Return Value

## Objective of the Program
# To understand how to pass multiple arguments to a function and return the result using the `return` statement.

## Lab
# A Python function can accept multiple parameters. The values passed to these
# parameters are used to perform an operation, and the result can be returned using 
# the `return` statement.

## Program

def multiply(x, y):
    return x * y

result = multiply(3, 4)  # The function returns 12

print(result)

## Output

# 12


## Key Points

# 1. `x` and `y` are parameters of the function.
# 2. `3` and `4` are arguments passed to the function.
# 3. `return x * y` calculates and returns the product.
# 4. `multiply(3, 4)` returns `12`.
# 5. The returned value is stored in the variable `result`.
# 6. `print(result)` displays the returned value.
# 7. A function can have multiple parameters.
# 8. The `return` statement allows the result of a function to be used elsewhere in the program.
