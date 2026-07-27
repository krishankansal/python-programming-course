# Lab 22: Number Guessing Game using continue
# Objective : To learn how to skip the current iteration using the continue statement.

import random

secret = random.randint(100, 999)
chance = 1

print("Guess the 3-digit secret number.")
print("You have 10 chances.")
print("Only 3-digit numbers are accepted.\n")

while chance <= 10:

    guess = int(input(f"Chance {chance}: Enter your guess: "))

    if guess < 100 or guess > 999:
        print("Invalid Input! Please enter a 3-digit number.")
        continue

    if guess == secret:
        print("\nCongratulations! You guessed the secret number.")
        break

    elif guess < secret:
        print("Too Small")

    else:
        print("Too Large")

    chance = chance + 1

else:
    print("\nGame Over!")
    print("The secret number was:", secret)

# Key Notes
# 1. continue skips the remaining statements of the current iteration.
# 2. When an invalid number is entered, the loop immediately starts the next iteration.
# 3. Statements after continue are not executed for that iteration.
# 4. Unlike break, continue does not terminate the loop.
# 5. continue is useful for ignoring invalid or unwanted input.