# Lab No. 80: Checking Whether a Number is Prime
#
# Objective:
# To determine whether a number is prime by using a function that
# finds its factors.

# Program

from f012 import *


def isprime(n):
    if factors(n) == [1, n]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isprime(13))


# -----------------------------
# Key Points
# -----------------------------
# 1. A prime number has exactly two factors: 1 and the number itself.
# 2. The factors() function is imported from f012.
# 3. factors(n) is compared with [1, n].
# 4. The function returns True when the number is prime.
# 5. Otherwise, it returns False.
# 6. __name__ == "__main__" controls direct execution of the program.
