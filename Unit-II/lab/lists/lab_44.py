# Lab 44: List Methods in Python
# Objective:
# To learn commonly used list methods such as count(), index(),
# reverse(), and sort().

# 1. Using count()
numbers = [10, 20, 10, 30, 10, 40]

print("Number of times 10 occurs:")
print(numbers.count(10))

# 2. Using index()
students = ["Alice", "Bob", "Charlie", "David"]

print("\nIndex of Charlie:")
print(students.index("Charlie"))

# 3. Using reverse()
numbers = [10, 20, 30, 40]

numbers.reverse()

print("\nList after reverse():")
print(numbers)

# 4. Using sort()
marks = [78, 45, 92, 61, 88]

marks.sort()

print("\nMarks in Ascending Order:")
print(marks)

# 5. Sorting in descending order
marks.sort(reverse=True)

print("\nMarks in Descending Order:")
print(marks)

# Key Notes
# 1. count() returns the number of occurrences of a value.
# 2. index() returns the position of the first occurrence of a value.
# 3. reverse() reverses the existing list.
# 4. sort() sorts the existing list.
# 5. sort(reverse=True) sorts the list in descending order.
# 6. sort() modifies the original list.
# 7. sorted() and sort() are different: sorted() returns a new list,
#    while sort() modifies the existing list.