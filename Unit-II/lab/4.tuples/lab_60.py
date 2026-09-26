# Lab No. 60: Tuple Operations
#
# Objective:
# To learn different operations that can be performed on tuples.

# Program

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Tuple 1:")
print(tuple1)

print("\nTuple 2:")
print(tuple2)

print("\nAfter Concatenation:")
print(result)

# Tuple Repetition
numbers = (1, 2, 3)

result = numbers * 3

print("\nOriginal Tuple:")
print(numbers)

print("\nAfter Repetition:")
print(result)

# Membership Operator
fruits = ("Apple", "Banana", "Mango", "Orange")

print("\nFruits:")
print(fruits)

print("\nIs Mango present?")
print("Mango" in fruits)

print("\nIs Grapes present?")
print("Grapes" in fruits)

# Not-in Operator
print("\nIs Grapes not present?")
print("Grapes" not in fruits)

print("\nIs Apple not present?")
print("Apple" not in fruits)

# Comparing Tuples
tuple1 = (10, 20, 30)
tuple2 = (10, 20, 40)

print("\nTuple 1:")
print(tuple1)

print("Tuple 2:")
print(tuple2)

print("\nAre the tuples equal?")
print(tuple1 == tuple2)

print("\nIs Tuple 1 smaller than Tuple 2?")
print(tuple1 < tuple2)

print("\nIs Tuple 1 greater than Tuple 2?")
print(tuple1 > tuple2)

# Comparing Two Tuples with the Same Values
tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)

print("\nAre these tuples equal?")
print(tuple1 == tuple2)

# Finding the Length of a Tuple
numbers = (10, 20, 30, 40, 50)

print("\nNumbers:")
print(numbers)

print("\nLength of Tuple:")
print(len(numbers))

# Combining Different Operations
a = ("Python", "Java")
b = ("C", "C++")

combined = a + b
repeated = a * 2

print("\nCombined Tuple:")
print(combined)

print("\nRepeated Tuple:")
print(repeated)


# -----------------------------
# Key Points
# -----------------------------
# 1. The + operator is used to concatenate two tuples.
# 2. The * operator is used to repeat a tuple.
# 3. The in operator checks whether an element exists in a tuple.
# 4. The not in operator checks whether an element does not exist.
# 5. Tuples can be compared using comparison operators.
# 6. Tuple comparison is performed element by element.
# 7. len() returns the number of elements in a tuple.
# 8. Tuple operations do not modify the original tuple.
# 9. Since tuples are immutable, + and * create new tuples.
