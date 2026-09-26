# Lab No. 97: Login Required Decorator
#
# Objective:
# To understand how a decorator can be used to execute common
# login-related actions before and after a function.

# Program

def login_required(func):

    def check():
        print("You are logged in")
        func()
        print("You are logged out")

    return check


@login_required
def view_product():
    print("I am viewing page")


@login_required
def purchase():
    print("I am purchasing page")


view_product()
print("*" * 20)
purchase()


# -----------------------------
# Key Points
# -----------------------------
# 1. login_required() is a decorator function.
# 2. check() performs actions before and after the original function.
# 3. @login_required decorates both view_product() and purchase().
# 4. The original function is called between the login and logout messages.
# 5. The same decorator can be reused with multiple functions.
# 6. Decorators are useful for applying common behavior to several functions.
