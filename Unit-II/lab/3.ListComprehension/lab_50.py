# Lab No. 50: List Comprehension with Strings
#
# Objective:
# To create a list of characters from a string using a traditional
# for loop, list comprehension, and map() with lambda.

# Program

letters = []

for letter in 'human':
    letters.append(letter)

print(letters)

letters = [letter for letter in 'human']
print(letters)

# Using map() with lambda function
letters = list(map(lambda x: x, 'human'))
print(letters)


# -----------------------------
# Key Points
# -----------------------------
# 1. A string is iterable, so its characters can be processed one by one.
# 2. List comprehension provides a concise alternative to a for loop.
# 3. map() applies a function to each item of an iterable.
# 4. lambda creates a small anonymous function.
