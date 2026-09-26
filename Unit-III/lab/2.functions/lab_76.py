# Function with *args (Variable Arguments)

def calculate_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(calculate_total(1, 2, 3))  # Output: 6
print(calculate_total(10, 20, 30, 40))  # Output: 100
