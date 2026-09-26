# Lab No. 92: Passing a Function as an Argument
#
# Objective:
# To understand that functions are objects in Python and can be
# passed as arguments to other functions.

# Program

def a():
    print("Hi, it's me 'a()'")
    print("Thanks for calling me")


def b(x):
    print("Hi, it's me 'b()'")
    print("I will call 'a()' now")
    x()

    # The real name of the function
    print("func's real name is " + x.__name__")
    return x


# b(a)
y = b(a)
y()


# -----------------------------
# Key Points
# -----------------------------
# 1. Functions are first-class objects in Python.
# 2. Function a is passed as an argument to function b.
# 3. x receives the function object a.
# 4. x() calls the function passed to b().
# 5. __name__ gives the name of the function object.
# 6. b() returns the function object, which is stored in y.
