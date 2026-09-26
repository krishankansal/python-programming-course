# Lab No. 90: Closure and Factory Function
#
# Objective:
# To understand how a function can create and return another function
# that remembers a value from the enclosing function.

# Program

def make_multiplier_of(n):

    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier_of(3)
print(times3(3))

times5 = make_multiplier_of(5)
print(times5(5))

print(times5(times3(2)))


# -----------------------------
# Key Points
# -----------------------------
# 1. make_multiplier_of() is a factory function.
# 2. multiplier() is a nested function.
# 3. The nested function uses n from the enclosing function.
# 4. times3 and times5 are different function objects created with different values of n.
# 5. Each returned function remembers the value supplied to the outer function.
# 6. A closure allows the returned function to retain access to its enclosing data.
