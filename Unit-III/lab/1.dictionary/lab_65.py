# Lab No. 65: Updating a Dictionary
#
# Objective:
# To understand how to update the value of an existing dictionary key
# and add a new key-value pair.

# Program

students = {
    "Laveneesh": 90,
    "Rohit": 65,
    "Amit": 75,
    "Suresh": 80,
    "nilesh": 55
}

# Updating the value of an existing key
students["Laveneesh"] = 40

print(students)

# Adding a new key-value pair
students["kartik"] = 77

print(students)


# -----------------------------
# Key Points
# -----------------------------
# 1. A dictionary value can be updated using its key.
# 2. Assigning a new value to an existing key replaces the old value.
# 3. A new key-value pair can be added using assignment.
# 4. Dictionary keys are used to identify and modify values.
# 5. The print() function displays the updated dictionary.
