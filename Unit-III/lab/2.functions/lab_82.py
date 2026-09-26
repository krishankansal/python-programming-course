# Lab No. 82: Assigning a Function to a Variable
#
# Objective:
# To understand that a function can be assigned to another variable
# and called using that variable.

# Program

def first():
    print("Function Assignment Example")


second = first

print(second)
second()


# -----------------------------
# Key Points
# -----------------------------
# 1. Functions are objects in Python.
# 2. A function can be assigned to another variable.
# 3. second = first makes both names refer to the same function object.
# 4. second() calls the function through the new variable.
# 5. print(second) displays the function object representation.
