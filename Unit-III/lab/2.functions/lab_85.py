# Lab No. 85: Nested Functions
#
# Objective:
# To understand how a function can be defined inside another function
# and how the outer function can call the inner function.

# Program

def outer():

    def inner():
        print("Hi, it's me 'inner'")
        print("Thanks for calling me")

    print("This is the function 'outer'")
    print("I am calling 'inner' now:")
    inner()


outer()


# -----------------------------
# Key Points
# -----------------------------
# 1. A function can be defined inside another function.
# 2. The inner function is called a nested function.
# 3. inner() is defined inside outer().
# 4. The outer function can call the inner function.
# 5. Calling outer() executes the statements in outer and then inner.
