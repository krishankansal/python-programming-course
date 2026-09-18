lst = []

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
factors(12)
print("Factors of 12 are:",lst)


def factors1(n):
    lst1 = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst1.append(i)
    return lst1

print("Factors of 12 are:",factors1(12))

def is_prime(n):
    l = factors1(n)
    if len(l) == 2:
         print(n,"is a prime number")
    else:
         print(n,"is not a prime number")

is_prime(170)