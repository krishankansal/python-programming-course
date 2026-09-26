# Lab 32: Membership Operators in Python
# Objective:
# To learn how to use membership operators (in and not in) with strings.

text = "Python Programming"

print("Original String:")
print(text)

# -----------------------------------------
# 1. Checking a Character
# -----------------------------------------

print("\nChecking a Character:")

print("'P' in text:")
print('P' in text)

print("'Z' in text:")
print('Z' in text)

# -----------------------------------------
# 2. Checking a Word
# -----------------------------------------

print("\nChecking a Word:")

print("'Python' in text:")
print("Python" in text)

print("'Java' in text:")
print("Java" in text)

# -----------------------------------------
# 3. Using not in
# -----------------------------------------

print("\nUsing not in:")

print("'Java' not in text:")
print("Java" not in text)

print("'Programming' not in text:")
print("Programming" not in text)

# -----------------------------------------
# 4. Case Sensitivity
# -----------------------------------------

print("\nCase Sensitivity:")

print("'python' in text:")
print("python" in text)

print("'Python' in text:")
print("Python" in text)

# -----------------------------------------
# 5. Practical Example - Email Validation
# -----------------------------------------

email = "student@gmail.com"

print("\nChecking Email Address:")

print("'@' in email:")
print("@" in email)

print("'.com' in email:")
print(".com" in email)

# -----------------------------------------
# 6. Practical Example - Website URL
# -----------------------------------------

website = "https://www.python.org"

print("\nChecking Website URL:")

print("'https' in website:")
print("https" in website)

print("'http' not in website:")
print("http://" not in website)

# -----------------------------------------
# Key Notes
# -----------------------------------------

# 1. The 'in' operator checks whether a character or substring exists in a string.
# 2. The 'not in' operator checks whether a character or substring does not exist in a string.
# 3. Membership operators return either True or False.
# 4. Membership checking is case-sensitive.
# 5. Both characters and complete words can be searched.
# 6. Membership operators are commonly used in searching, validation, and filtering text.
# 7. These operators do not modify the original string.