# Lab 21: Number Guessing Game using break
# Objective : To learn how to terminate a loop using the break statement.

import random

secret = random.randint(100, 999)
chance = 1

print("Guess the 3-digit secret number.")
print("You have only 6 chances.\n")

while chance <= 6:

    guess = int(input(f"Chance {chance}: Enter your guess: "))

    if guess == secret:
        print("\nCongratulations! You guessed the secret number.")
        break

    elif guess < secret:
        print("Too Small")

    else:
        print("Too Large")

    chance = chance + 1

else:
    print("\nSorry! You have used all 6 chances.")
    print("The secret number was:", secret)

# Key Notes
# 1. random.randint(100, 999) generates a random 3-digit number.
# 2. The player gets a maximum of 6 chances to guess the number.
# 3. break immediately terminates the loop when the correct number is guessed.
# 4. The else block executes only if the loop finishes without encountering break.
# 5. This is a practical application of break in game development.

"""
Understanding else with while

In Python, a while loop can have an optional else block.

The else block executes only when the loop finishes normally, i.e., when the loop condition becomes False.
If the loop is terminated using the break statement, the else block is not executed.
In this program:
If the user guesses the correct number within 6 chances, the break statement is executed.
As soon as break is executed, the loop terminates immediately, so the else block is skipped.
If the user fails to guess the number in all 6 chances, the loop ends because chance becomes 7 (chance <= 6 becomes False).
Since the loop ended normally (without break), the else block executes and displays:
"""