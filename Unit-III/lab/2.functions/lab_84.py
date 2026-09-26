# Lab No. 84: Assigning a Function to Another Variable
#
# Objective:
# To understand how a function can be assigned to another variable
# and invoked using the new variable.

# Program

def increment(x):
    return x + 1


successor = increment

print('successor of 10 is :', successor(10))


# -----------------------------
# Key Points
# -----------------------------
# 1. increment is a function that returns x + 1.
# 2. successor = increment assigns the function to another variable.
# 3. successor refers to the same function object as increment.
# 4. successor(10) calls the function with 10 as the argument.
# 5. The returned result is 11.
