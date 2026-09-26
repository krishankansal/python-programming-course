# Lab No. 77: Function with **kwargs (Keyword Arguments)
#
# Objective:
# To understand how **kwargs allows a function to accept a variable
# number of keyword arguments.

# Program

def create_profile(**details):
    print("User Profile:")

    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")


create_profile(
    name="Alice",
    age=30,
    profession="Engineer",
    city="Mumbai"
)


# -----------------------------
# Key Points
# -----------------------------
# 1. **kwargs allows a variable number of keyword arguments.
# 2. Inside the function, details is a dictionary.
# 3. items() provides each key-value pair for iteration.
# 4. key.capitalize() converts the first character of the key to uppercase.
# 5. Different keyword arguments can be supplied in the same function call.
