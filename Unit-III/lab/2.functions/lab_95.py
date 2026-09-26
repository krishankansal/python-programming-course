# Lab No. 95: Decorator with Conditional Logic
#
# Objective:
# To understand how a decorator can control whether the original
# function is called based on a condition.

# Program

def legends(func):

    def checkker(name):
        if name == 'Mountbatten':
            print('Mountbatten Was not an indian legend')
        else:
            func(name)

    return checkker


@legends
def indian_legends(name):
    print(name, 'Was a indian legend')


indian_legends('Swami Vivekanand')
indian_legends('Mahatma Gandhi')
indian_legends('Mountbatten')
indian_legends('Aarya Bhatt')


# -----------------------------
# Key Points
# -----------------------------
# 1. legends() is a decorator function.
# 2. checkker() receives the argument passed to the decorated function.
# 3. The decorator checks the value of name before calling the original function.
# 4. For Mountbatten, the original function is not called.
# 5. For other names, func(name) executes the original function.
# 6. Decorators can be used to add validation or conditional behavior.
