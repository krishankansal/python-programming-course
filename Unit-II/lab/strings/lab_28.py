# Lab 28: join() Method in Python
# Objective:
# To learn how to join the elements of a list into a single string using the join() method.

# Example 1: Joining words with a space
words = ["Python", "is", "easy"]

print("Original List:")
print(words)

print("\nJoining with Space:")
print(" ".join(words))


# Example 2: Joining words with a hyphen
print("\nJoining with Hyphen:")
print("-".join(words))


# Example 3: Joining words with a comma
print("\nJoining with Comma:")
print(", ".join(words))


# Example 4: Joining letters into a word
letters = ['P', 'Y', 'T', 'H', 'O', 'N']

print("\nJoining Letters:")
print("".join(letters))


# Example 5: Joining characters of a string
text = "Python"

print("\nJoining Characters with *:")
print("*".join(text))


# Example 6: Creating a file path
folders = ["Users", "Krishan", "Documents", "Python"]

print("\nFile Path:")
print("/".join(folders))


# Example 7: Creating a CSV Record
student = ["101", "Aman", "BCA", "85"]

print("\nCSV Record:")
print(",".join(student))


# Example 8: Creating a Website URL
parts = ["https://", "www", "python", "org"]

print("\nWebsite URL:")
print(".".join(parts))


# Example 9: Joining Fruits
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("\nFruit List:")
print(" | ".join(fruits))


# Example 10: Joining Numbers
numbers = ["10", "20", "30", "40", "50"]

print("\nNumbers:")
print(" - ".join(numbers))


# Key Notes
# 1. The join() method combines all elements of an iterable into a single string.
# 2. Syntax: separator.join(iterable)
# 3. The separator can be a space, comma, hyphen, slash, or any string.
# 4. All elements of the iterable must be strings.
# 5. join() returns a new string and does not modify the original list.
# 6. join() works with lists, tuples, and other iterables containing strings.
# 7. join() is commonly used to create sentences, file paths, URLs, CSV records, and formatted output.