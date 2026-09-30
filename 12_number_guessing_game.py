# 12. Number Guessing Game

"""
Generate a random number between 1–100. Keep asking the user to guess until they find the correct number. 
After each incorrect guess, display "Too High" or "Too Low". Finally display the number of attempts taken.
"""

# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 100. This number is hidden from the user
secret_number = random.randint(1, 100)

# Counter to keep track of the number of guesses
attempts = 0

# Display the game instructions
print("I have selected a number between 1 and 100.")

# Keep asking the user for guesses until the correct number is found
while True:

    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Increase the attempt counter by 1
    attempts += 1

    # Check if the guess is smaller than the secret number
    if guess < secret_number:
        print("Too Low")

    # Check if the guess is greater than the secret number
    elif guess > secret_number:
        print("Too High")

    # If neither condition is true, the guess must be correct
    else:
        print("Correct!")

        # Display the total number of attempts
        print("Number of attempts:", attempts)

        # Stop the while loop
        break