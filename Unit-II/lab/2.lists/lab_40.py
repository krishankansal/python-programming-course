# Lab 40: Removing Elements from a List
# Objective:
# To learn different methods for removing elements from a list.

# 1. Removing an element using remove()
students = ["Alice", "Bob", "Charlie", "David"]

students.remove("Charlie")

print("After remove():")
print(students)

# 2. Removing the last element using pop()
removed_student = students.pop()

print("\nRemoved Element using pop():")
print(removed_student)

print("List after pop():")
print(students)

# 3. Removing an element using its index
removed_student = students.pop(1)

print("\nRemoved Element at Index 1:")
print(removed_student)

print("List after pop(1):")
print(students)

# 4. Removing an element using del
numbers = [10, 20, 30, 40]

del numbers[1]

print("\nAfter using del:")
print(numbers)

# 5. Removing all elements using clear()
numbers.clear()

print("\nAfter using clear():")
print(numbers)

# Key Notes
# 1. remove(value) removes a specific value from the list.
# 2. pop() removes and returns the last element.
# 3. pop(index) removes and returns the element at the specified index.
# 4. del can be used to delete an element or a portion of a list.
# 5. clear() removes all elements from the list.