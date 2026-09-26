# LAB 63: Passing Different Data Types

## Objective of the Program

# To understand how different data types, such as lists, can be passed as arguments to a Python function.

## Lab

# Python functions can accept different types of data as arguments. A list can be passed to a function, and the function can process each element of the list using a `for` loop.

## Program

def process_list(items):
    for item in items:
        print(item)


fruits = ["apple", "banana", "cherry"]

process_list(fruits)

## Output

# apple
# banana
# cherry

## Key Points

# 1. A list can be passed as an argument to a function.
# 2. `items` is the parameter that receives the list.
# 3. `fruits` is a list containing three string values.
# 4. `process_list(fruits)` passes the `fruits` list to the function.
# 5. The `for` loop accesses each element of the list one by one.
# 6. `item` represents the current element during each iteration.
# 7. `print(item)` displays each element of the list.
# 8. Python functions can work with different data types such as strings, numbers, lists, tuples, and dictionaries.

