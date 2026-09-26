# Lab No. 89: Closures and Returning a Function
#
# Objective:
# To understand how a nested function can be returned from an outer
# function and used outside the scope of the outer function.

# Program

def outer(text):
    text = text

    def inner():
        print(text)

    return inner  # Returning the function without parentheses


funct = outer('Example of closure')
funct()


# -----------------------------
# Key Points
# -----------------------------
# 1. A closure requires a nested function.
# 2. The enclosing function returns the nested function.
# 3. inner is returned without parentheses because the function itself is returned.
# 4. The returned function is assigned to funct.
# 5. funct() can then be called outside outer().
# 6. The inner function retains access to text from the enclosing scope.
