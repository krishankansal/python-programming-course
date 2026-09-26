# Lab No. 73: Function with Default Parameters
#
# Objective:
# To understand how default parameter values are used when arguments
# are not supplied during a function call.

# Program

def introduce(name, age=25, city="Unknown"):
    print(f"Hi, I'm {name}, {age} years old, from {city}")


introduce("Allice")
introduce("Bob", 30)
introduce("Charlie", 28, "New York")


# -----------------------------
# Key Points
# -----------------------------
# 1. Default parameters have predefined values.
# 2. The default value is used when the corresponding argument is omitted.
# 3. age has a default value of 25.
# 4. city has a default value of "Unknown".
# 5. Supplied arguments replace the corresponding default values.
