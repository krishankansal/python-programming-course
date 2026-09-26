# Lab 27: String Built-in Functions in Python
# Objective:
# To learn commonly used built-in functions for strings.

text = "Python Programming"

print("Original String:")
print(text)

# 1. len() Function
print("\nLength of String:")
print(len(text))

# 2. max() Function
print("\nMaximum Character:")
print(max(text))

# 3. min() Function
print("\nMinimum Character:")
print(min(text))

# 4. sorted() Function
print("\nSorted Characters:")
print(sorted(text))

# 5. Converting sorted list into a string
sorted_text = "".join(sorted(text))

print("\nSorted String:")
print(sorted_text)

# Key Notes
# 1. len() returns the total number of characters in a string, including spaces.
# 2. max() returns the character with the highest Unicode (ASCII) value.
# 3. min() returns the character with the lowest Unicode (ASCII) value.
# 4. sorted() returns a list containing the characters of the string in ascending order.
# 5. The sorted() function does not modify the original string.
# 6. The join() method combines the characters of a list into a single string.
# 7. Strings are immutable, so these functions return new values without changing the original string.