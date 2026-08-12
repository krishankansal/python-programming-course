# Lab 26: String Indexing and Slicing in Python
# Objective:
# To learn how to access individual characters and extract substrings using indexing and slicing.

text = "Python Programming"

print("Original String:")
print(text)

print("\nLength of String:")
print(len(text))

# -------------------------------
# Positive Indexing
# -------------------------------
print("\nPositive Indexing:")
print("First Character           :", text[0])
print("Fourth Character          :", text[3])
print("Last Character (Positive) :", text[len(text)-1])

# -------------------------------
# Negative Indexing
# -------------------------------
print("\nNegative Indexing:")
print("Last Character            :", text[-1])
print("Second Last Character     :", text[-2])
print("Fifth Last Character      :", text[-5])

# -------------------------------
# Basic Slicing
# -------------------------------
print("\nBasic Slicing:")

print("text[0:6]   :", text[0:6])
print("text[:6]    :", text[:6])
print("text[7:]    :", text[7:])
print("text[:]     :", text[:])

# -------------------------------
# Middle Portion
# -------------------------------
print("\nMiddle Slicing:")

print("text[3:10]  :", text[3:10])
print("text[2:15]  :", text[2:15])

# -------------------------------
# Slicing with Step
# -------------------------------
print("\nSlicing with Step:")

print("text[::2]   :", text[::2])
print("text[::3]   :", text[::3])
print("text[1::2]  :", text[1::2])

# -------------------------------
# Reverse Slicing
# -------------------------------
print("\nReverse Slicing:")

print("text[::-1]  :", text[::-1])
print("text[::-2]  :", text[::-2])

# -------------------------------
# Negative Indices in Slicing
# -------------------------------
print("\nNegative Index Slicing:")

print("text[-11:]      :", text[-11:])
print("text[:-12]      :", text[:-12])
print("text[-18:-12]   :", text[-18:-12])

# -------------------------------
# Key Notes
# -------------------------------
# 1. Indexing is used to access a single character of a string.
# 2. Positive indexing starts from 0 and moves from left to right.
# 3. Negative indexing starts from -1 and moves from right to left.
# 4. Slicing extracts a part (substring) of a string.
# 5. Syntax of slicing is string[start : stop : step].
# 6. The start index is included, but the stop index is excluded.
# 7. Omitting the start index means slicing begins from the first character.
# 8. Omitting the stop index means slicing continues to the last character.
# 9. Omitting both start and stop (text[:]) returns the complete string.
# 10. The step value specifies how many characters to skip.
# 11. A negative step slices the string in reverse order.
# 12. Strings are immutable; slicing always creates a new string.