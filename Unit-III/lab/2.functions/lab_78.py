# Lab No. 78: Function with Both *args and **kwargs
#
# Objective:
# To understand how a function can accept both variable positional
# arguments and variable keyword arguments.

# Program

def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


flexible_function(1, 2, 3, name="John", age=25)


# -----------------------------
# Key Points
# -----------------------------
# 1. *args collects variable positional arguments.
# 2. **kwargs collects variable keyword arguments.
# 3. args is represented as a tuple inside the function.
# 4. kwargs is represented as a dictionary inside the function.
# 5. Both can be used together in the same function.
