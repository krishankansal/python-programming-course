# Lab No. 93: Function Decorator
#
# Objective:
# To understand the basic use of a decorator to add functionality
# to an existing function.

# Program

def get_loaded(func):

    def inner():
        print("First line added")
        func()
        print("I am loaded")

    return inner


@get_loaded
def rifle():
    print("T-5000 sniper rifle")


rifle()


# Equivalent decorator operation:
# rifle = get_loaded(rifle)
# rifle()


# -----------------------------
# Key Points
# -----------------------------
# 1. A decorator is a function that modifies or extends another function.
# 2. get_loaded() accepts a function as an argument.
# 3. inner() adds statements before and after the original function.
# 4. @get_loaded applies the decorator to rifle().
# 5. Calling rifle() actually executes the decorated function.
# 6. The decorator syntax is an alternative to explicitly reassigning the function.
