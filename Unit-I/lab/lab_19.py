# Lab 19: Star Pattern using Nested Loops
# Objective : To learn how to use nested for loops to generate star (*) patterns.

rows = int(input("Enter the number of rows: "))

print("\nStar Pattern")
print("------------")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Key Notes
# 1. A nested loop is a loop inside another loop.
# 2. The outer loop controls the number of rows.
# 3. The inner loop controls the number of stars printed in each row.
# 4. The end=" " argument prints stars on the same line.
# 5. print() without arguments moves the cursor to the next line.