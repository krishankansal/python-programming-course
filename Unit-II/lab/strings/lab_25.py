# Lab 25: Basic String Operations in Python
# Objective:
# To learn basic operations on strings such as concatenation and repetition.

# 1. String Concatenation using + operator
first_name = "Alice"
last_name = "Johnson"

print("Concatenation using + operator:")
print(first_name + last_name)

# 2. Printing strings using comma (,)
print("\nPrinting using comma:")
print(first_name, last_name)

# 3. String Repetition using * operator
separator = "-" * 20

print("\nString Repetition:")
print(separator)

# 4. Repeating a word
emphasis = "Very " * 3 + "Important!"

print("\nRepeated String:")
print(emphasis)

# 5. Creating a Banner
banner = "=" * 10 + " WELCOME " + "=" * 10

print("\nBanner:")
print(banner)

# Key Notes
# 1. The + operator is used to concatenate (join) two or more strings.
# 2. The * operator repeats a string a specified number of times.
# 3. The comma (,) in the print() function automatically inserts a space between values.
# 4. String concatenation creates a new string without modifying the original strings.
# 5. The repetition operator (*) is useful for creating separators, borders, and banners.
# 6. Strings are immutable, so every operation creates a new string.