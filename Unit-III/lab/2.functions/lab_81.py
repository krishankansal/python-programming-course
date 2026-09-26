# Lab No. 81: Multiplication Table Using a Function
#
# Objective:
# To define and call a function that displays the multiplication
# table of a given number.

# Program

def mul_table(n):
    num = 1

    for i in range(1, 11):
        print(n, 'x', num, '=', i * n)
        num = num + 1


mul_table(13)


# -----------------------------
# Key Points
# -----------------------------
# 1. mul_table() is a user-defined function.
# 2. n is the parameter that receives the number.
# 3. The for loop generates ten multiplication results.
# 4. num keeps track of the multiplier.
# 5. The function is called using mul_table(13).
