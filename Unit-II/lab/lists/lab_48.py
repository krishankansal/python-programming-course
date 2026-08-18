# Lab 48: Menu-Driven List Application
# Objective:
# To develop a menu-driven Python program that demonstrates
# common list operations.

# Creating an empty list
students = []

while True:

    print("\n----- Student List Menu -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Sort Students")
    print("6. Count Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Student
    if choice == 1:

        name = input("Enter student name: ")

        students.append(name)

        print("Student added successfully.")

    # 2. Display Students
    elif choice == 2:

        print("\nStudents:")

        for student in students:
            print(student)

    # 3. Search Student
    elif choice == 3:

        name = input("Enter student name to search: ")

        if name in students:
            print("Student Found")
        else:
            print("Student Not Found")

    # 4. Remove Student
    elif choice == 4:

        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed successfully.")
        else:
            print("Student Not Found")

    # 5. Sort Students
    elif choice == 5:

        students.sort()

        print("Students sorted successfully.")

    # 6. Count Students
    elif choice == 6:

        print("Total Students:", len(students))

    # 7. Exit
    elif choice == 7:

        print("Program ended.")
        break

    # Invalid choice
    else:

        print("Invalid choice.")

# Key Notes
# 1. A list can be dynamically modified while a program is running.
# 2. append() is used to add new students.
# 3. remove() is used to remove a student.
# 4. The in operator is used for searching.
# 5. sort() is used to arrange the list.
# 6. len() is used to count the number of elements.
# 7. A while loop can be combined with lists to create menu-driven applications.
# 8. This program integrates several concepts learned throughout the Lists topic.