# Lab No. 55: if-else with List Comprehension
#
# Objective:
# To use if-else within list comprehension to classify numbers as
# Even or Odd.

# Program

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)


# -----------------------------
# Key Points
# -----------------------------
# 1. List comprehension can contain an if-else expression.
# 2. The condition i % 2 == 0 checks whether a number is even.
# 3. "Even" is selected when the condition is True.
# 4. "Odd" is selected when the condition is False.
