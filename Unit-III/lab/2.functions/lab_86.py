# Lab No. 86: Calling a Nested Function
#
# Objective:
# To understand how an inner function is defined and called from
# within an outer function.

# Program

def outer():  # outer function
    print("Hello from outer function")

    def inner():  # inner function
        print("Hello from inner function")

    inner()


outer()

# The following statements are not valid ways to access the inner function:
# outer.inner
# outer.inner()
# outer().inner
# outer().inner()


# -----------------------------
# Key Points
# -----------------------------
# 1. A function can be defined inside another function.
# 2. The outer function is called outer().
# 3. The inner function is defined inside outer().
# 4. The inner function is called from within the outer function.
# 5. The inner function is local to the outer function.
