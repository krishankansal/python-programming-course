# Lab 30: String Methods-II in Python
# Objective:
# To learn commonly used string methods such as strip(), replace(), find(), and count().

# Original String
text = "   Python Programming with Python   "

print("Original String:")
print("'" + text + "'")

# 1. strip() Method
print("\nstrip() Method:")
print("'" + text.strip() + "'")

# 2. lstrip() Method
print("\nlstrip() Method:")
print("'" + text.lstrip() + "'")

# 3. rstrip() Method
print("\nrstrip() Method:")
print("'" + text.rstrip() + "'")

# 4. replace() Method
print("\nreplace() Method:")
print(text.replace("Python", "Java"))

# 5. find() Method
print("\nfind() Method:")
print("Position of 'Programming':", text.find("Programming"))

print("Position of 'Java':", text.find("Java"))

# 6. count() Method
print("\ncount() Method:")
print("Count of 'Python':", text.count("Python"))

print("Count of 'a':", text.count("a"))

# Key Notes
# 1. strip() removes spaces from both the beginning and the end of a string.
# 2. lstrip() removes spaces only from the left side of a string.
# 3. rstrip() removes spaces only from the right side of a string.
# 4. replace(old, new) replaces all occurrences of the old substring with the new substring.
# 5. find(substring) returns the index of the first occurrence of the substring.
# 6. If the substring is not found, find() returns -1.
# 7. count(substring) returns the total number of occurrences of the specified substring.
# 8. These methods return new strings or values without modifying the original string.
# 9. Strings are immutable, so the original string remains unchanged.