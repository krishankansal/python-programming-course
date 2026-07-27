# Lab 11: Electricity Bill Calculator using if-elif-else
# Objective : To learn how to solve a real-world problem using the if-elif-else statement.

units = int(input("Enter electricity units consumed: "))

print("\nElectricity Bill")
print("----------------")

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

print("Units Consumed :", units)
print("Total Bill     : ₹", bill)

# Key Notes
# 1. if-elif-else is used to evaluate multiple conditions.
# 2. Only one condition block is executed.
# 3. Real-world billing often uses slab-wise calculations.
# 4. Variables can store intermediate calculations for better readability.
# 5. Python is widely used to automate billing and business applications.