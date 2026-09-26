# Lab No. 70: Passing Different Data Types to a Function
#
# Objective:
# To understand how different data types, such as lists, can be
# passed as arguments to a Python function.

# Program

def process_list(items):
    for item in items:
        print(item)


fruits = ["apple", "banana", "cherry"]

process_list(fruits)


# -----------------------------
# Key Points
# -----------------------------
# 1. A list can be passed as an argument to a function.
# 2. items is the parameter that receives the list.
# 3. fruits is a list containing string values.
# 4. process_list(fruits) passes the list to the function.
# 5. The for loop accesses each element one by one.
# 6. Python functions can work with different data types.
