# Lab 53: Accessing Tuples
# Objective:
# To learn different ways of accessing elements from tuples
# using indexing and slicing.


# 1. Creating a tuple

subjects = ("Python", "DBMS", "Java", "AI", "Data Science")

print("Subjects:")
print(subjects)


# 2. Accessing the first element

print("\nFirst Subject:")
print(subjects[0])


# 3. Accessing the third element

print("\nThird Subject:")
print(subjects[2])


# 4. Accessing the last element using negative indexing

print("\nLast Subject:")
print(subjects[-1])


# 5. Accessing the second-last element

print("\nSecond Last Subject:")
print(subjects[-2])


# 6. Accessing the first three elements using slicing

print("\nFirst Three Subjects:")
print(subjects[0:3])


# 7. Accessing elements from the middle

print("\nMiddle Subjects:")
print(subjects[1:4])


# 8. Slicing from the beginning

print("\nSubjects from Beginning:")
print(subjects[:3])


# 9. Slicing up to the end

print("\nSubjects from Java onwards:")
print(subjects[2:])


# 10. Accessing the tuple in reverse

print("\nReverse Tuple:")
print(subjects[::-1])


# 11. Using a step value

print("\nAlternate Subjects:")
print(subjects[::2])


# 12. Nested tuple

student = (
    "Rahul",
    21,
    ("Python", "DBMS", "AI")
)

print("\nStudent:")
print(student)


# 13. Accessing an element from the nested tuple

print("\nStudent Name:")
print(student[0])

print("\nFirst Subject:")
print(student[2][0])

print("\nSecond Subject:")
print(student[2][1])


# Key Notes
# 1. Tuple elements are accessed using indexes.
# 2. Positive indexing starts from 0.
# 3. Negative indexing starts from -1.
# 4. Slicing is used to access a range of elements.
# 5. The syntax for slicing is tuple[start:stop:step].
# 6. The stop index is not included in the result.
# 7. A step value can be used to skip elements.
# 8. [::-1] is commonly used to reverse a tuple.
# 9. Tuples can contain other tuples.
# 10. Nested tuple elements can be accessed using multiple indexes.