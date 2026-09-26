# Lab No. 67: Accessing Dictionary Values using get()
#
# Objective:
# To understand the get() method for safely accessing a value from
# a dictionary when a key may or may not exist.

# Program

students = {
    "Laveneesh": 90,
    "Rohit": 65,
    "Amit": 75,
    "Suresh": 80,
    "nilesh": 55
}

# Accessing a key that does not exist
print(students.get("amit"))

# Providing a default value when the key is not found
print(students.get("amit", "Not Found"))


# -----------------------------
# Key Points
# -----------------------------
# 1. get() is used to access a dictionary value using its key.
# 2. If the requested key does not exist, get() returns None by default.
# 3. A default value can be supplied as the second argument to get().
# 4. get() is useful when a key may not exist in the dictionary.
# 5. Dictionary keys are case-sensitive, so "amit" and "Amit" are different keys.
