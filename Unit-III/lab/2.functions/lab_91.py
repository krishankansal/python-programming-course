# Lab No. 91: Closure for Permission Checking
#
# Objective:
# To understand how a closure can remember a value from its enclosing
# function and use it later when the returned function is called.

# Program

def has_permission(page_url):

    def inner(username):
        if username == 'Admin':
            return f"'{username}' does have access to {page_url}."
        else:
            return f"'{username}' does NOT have access to {page_url}."

    return inner


x = has_permission('http://www.banking.com')
print(x('Admin'))

y = has_permission('http://www.banking.com')
print(y('xyz'))


# -----------------------------
# Key Points
# -----------------------------
# 1. has_permission() is the enclosing function.
# 2. inner() is the nested function.
# 3. page_url is remembered by the returned inner function.
# 4. The username is checked when the returned function is called.
# 5. Different returned functions can be created for the same or different pages.
# 6. This demonstrates the practical use of closures.
