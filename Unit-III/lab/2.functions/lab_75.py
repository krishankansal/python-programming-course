# Lab No. 75: Function Returning a Dictionary
#
# Objective:
# To understand how a function can process a list of grades and
# return the results as a dictionary.

# Program

def process_grades(grades):
    total = sum(grades)
    average = total / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return {
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest
    }


student_grades = [85, 92, 78, 96, 88]
results = process_grades(student_grades)
print(results)


# -----------------------------
# Key Points
# -----------------------------
# 1. A function can return a dictionary.
# 2. sum() calculates the total of the grades.
# 3. len() is used to calculate the average.
# 4. max() and min() find the highest and lowest grades.
# 5. The calculated results are stored as key-value pairs in a dictionary.
