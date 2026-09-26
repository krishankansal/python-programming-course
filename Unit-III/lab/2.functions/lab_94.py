# Lab No. 94: Multiple Decorators
#
# Objective:
# To understand how multiple decorators can be applied to the same
# function.

# Program

def master_python(func):

    def python():
        func()
        print('Now Expert In Python')

    return python


def master_django(func):

    def django():
        func()
        print('Now Expert In Django')

    return django


# Equivalent decorator operations:
# programmer = master_django(programmer)
# programmer = master_python(programmer)

@master_django
@master_python
def programmer():
    print('I know programming concepts')


programmer()


# -----------------------------
# Key Points
# -----------------------------
# 1. A function can have more than one decorator.
# 2. @master_python and @master_django decorate programmer().
# 3. Multiple decorators are applied in nested order.
# 4. Each decorator adds its own functionality.
# 5. The decorated function is called using programmer().
