# Lab No. 74: Function Returning Multiple Values
#
# Objective:
# To understand how a function can return multiple values and how
# the returned values can be assigned to separate variables.

# Program

def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference


x, y = calculate_circle(5)
print(f"Area: {x:.2f}, Circumference: {y:.2f}")


# -----------------------------
# Key Points
# -----------------------------
# 1. A function can return more than one value.
# 2. return area, circumference returns two values.
# 3. x and y receive the returned values through unpacking.
# 4. The area of a circle is calculated using pi * radius * radius.
# 5. The circumference is calculated using 2 * pi * radius.
# 6. :.2f formats the output to two decimal places.
