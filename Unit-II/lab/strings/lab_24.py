# Lab 24: Creating Strings in Python
# Objective:
# To learn different ways of creating strings in Python.

# 1. Single-quoted string
single_string = 'Hello, World!'
print("Single-quoted String:")
print(single_string)

# 2. Double-quoted string
double_string = "Python Programming"
print("\nDouble-quoted String:")
print(double_string)

# 3. String containing both single and double quotes
mixed_quotes = """He said 'Hello' and she replied "Hi there!"."""
print("\nString with Mixed Quotes:")
print(mixed_quotes)

# 4. Multi-line string using triple quotes
multiline_string = """Welcome to Python.
This is a multi-line string.
Python preserves line breaks."""
print("\nMulti-line String:")
print(multiline_string)

# 5. Raw string
# # raw_string = r"C:\Program Files\Python\Scripts"
# print("\nRaw String:")
# print(raw_string)

# Key Notes
# 1. A string is a sequence of characters enclosed within quotes.
# 2. Strings can be created using single (' '), double (" "), or triple (''' ''' or """ """) quotes.
# 3. Triple quotes are used to create multi-line strings.
# 4. Raw strings are created by placing r before the opening quote and treat backslashes (\) as normal characters.
# 5. Strings are immutable, which means their contents cannot be changed after creation.
# 6. Strings are used to store and manipulate textual data in Python.