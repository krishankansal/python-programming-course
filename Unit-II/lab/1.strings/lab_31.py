# Lab 31: String Methods-III in Python
# Objective:
# To learn commonly used string methods such as split(), join(), startswith(), and endswith().

# -----------------------------------------
# 1. split() Method
# -----------------------------------------

text = "Python is easy to learn"

print("Original String:")
print(text)

print("\nsplit() using space:")
print(text.split())

fruits = "Apple,Mango,Banana,Orange"

print("\nsplit() using comma:")
print(fruits.split(","))

date = "05-08-2026"

print("\nsplit() using hyphen:")
print(date.split("-"))

# -----------------------------------------
# 2. join() Method
# -----------------------------------------

words = ["Python", "is", "easy"]

print("\nOriginal List:")
print(words)

print("\njoin() using space:")
print(" ".join(words))

print("\njoin() using hyphen:")
print("-".join(words))

print("\njoin() using comma:")
print(", ".join(words))

letters = ['P', 'Y', 'T', 'H', 'O', 'N']

print("\nJoining letters:")
print("".join(letters))

# -----------------------------------------
# 3. startswith() Method
# -----------------------------------------

text1 = "Python Programming"

print("\nstartswith() Method:")

print(text1.startswith("Python"))
print(text1.startswith("Java"))

# -----------------------------------------
# 4. endswith() Method
# -----------------------------------------

print("\nendswith() Method:")

print(text1.endswith("Programming"))
print(text1.endswith("Python"))

# -----------------------------------------
# Practical Examples
# -----------------------------------------

filename = "report.pdf"

print("\nChecking File Extension:")
print(filename.endswith(".pdf"))

email = "student@college.edu"

print("\nChecking Email Domain:")
print(email.endswith(".edu"))

website = "https://www.python.org"

print("\nChecking Website Protocol:")
print(website.startswith("https://"))

# -----------------------------------------
# Key Notes
# -----------------------------------------

# 1. split() divides a string into a list using a specified separator.
# 2. If no separator is given, split() uses spaces by default.
# 3. join() combines the elements of a list into a single string.
# 4. Syntax of join(): separator.join(iterable)
# 5. All elements of the iterable must be strings.
# 6. startswith() returns True if the string begins with the specified substring; otherwise, it returns False.
# 7. endswith() returns True if the string ends with the specified substring; otherwise, it returns False.
# 8. These methods are widely used in text processing, file handling, web development, and data analysis.
# 9. Strings are immutable, so these methods do not modify the original string.