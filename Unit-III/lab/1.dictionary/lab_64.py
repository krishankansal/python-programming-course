# Lab No. 64: Filtering Dictionary Elements
#
# Objective:
# To traverse a dictionary and print the names of students whose
# marks are greater than 70.

# Program

students = {
    "Laveneesh": 90,
    "Rohit": 65,
    "Amit": 75,
    "Suresh": 80,
    "nilesh": 55
}

for name, marks in students.items():
    if marks > 70:
        print(name)


# -----------------------------
# Key Points
# -----------------------------
# 1. items() is used to access both keys and values during iteration.
# 2. The variable name stores the student's name.
# 3. The variable marks stores the corresponding marks.
# 4. The if condition checks whether marks are greater than 70.
# 5. Only the names satisfying the condition are printed.
