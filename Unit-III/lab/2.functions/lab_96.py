# Lab No. 96: Authentication Decorator
#
# Objective:
# To understand how a decorator can be used to perform a simple
# authentication check before executing a function.

# Program

def autheticate(func):

    def inner(user):
        if user == 'kkk':
            print('Welcome', user)
            func(user)
        else:
            print('Please Login')

    return inner


@autheticate
def login(user):
    print("You Got an Email")


login('kkk')


# -----------------------------
# Key Points
# -----------------------------
# 1. autheticate() is a decorator that performs an authentication check.
# 2. inner() receives the username passed to login().
# 3. The original function runs only when the username is 'kkk'.
# 4. For another username, the decorator prints "Please Login".
# 5. @autheticate applies the decorator to login().
# 6. This demonstrates how decorators can control access to functions.
