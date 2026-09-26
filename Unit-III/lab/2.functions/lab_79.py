# Lab No. 79: Finding Factors of a Number
#
# Objective:
# To define a function that finds and returns all factors of a given number.

# Program

def factors(n):
    fact_list = []

    for i in range(1, n + 1):
        if n % i == 0:
            fact_list = fact_list + [i]

    return fact_list


if __name__ == "__main__":
    print(factors(22))


# -----------------------------
# Key Points
# -----------------------------
# 1. A factor divides a number exactly without leaving a remainder.
# 2. The range from 1 to n is checked for possible factors.
# 3. The modulo operator (%) checks whether a number divides n exactly.
# 4. Matching factors are added to fact_list.
# 5. The function returns the complete list of factors.
# 6. __name__ == "__main__" ensures the call runs when this file is executed directly.
