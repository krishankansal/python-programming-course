# Lab 22: pass Statement
# Objective : To learn how to use the pass statement as a placeholder.

marks = int(input("Enter student's marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    pass        # Grade calculation will be implemented later.

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: Fail")

print("Program Finished")

# Key Notes
# 1. pass is a null statement; it performs no action.
# 2. It is used as a placeholder where code will be written later.
# 3. pass prevents syntax errors when a block cannot be left empty.
# 4. Unlike break, pass does not terminate a loop.
# 5. Unlike continue, pass does not skip an iteration; execution simply proceeds to the next statement.