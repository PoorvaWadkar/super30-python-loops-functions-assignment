# 11. Password Retry System

"""
Store a predefined password and give the user a maximum of three attempts to enter it correctly. 
Use a while loop. After three incorrect attempts, display "Account Locked".
"""

# Store the correct password
correct_password = "Poorva@123"

# Counter to keep track of failed attempts
attempts = 0

# Maximum number of attempts allowed
max_attempts = 3

# Continue asking for the password while attempts are less than 3
while attempts < max_attempts:

    # Ask the user to enter the password
    password = input("Enter password: ")

    # Check whether the entered password matches the correct password
    if password == correct_password:
        print("Login successful.")

        # Stop the while loop because the password is correct
        break

    # Increase the failed attempt counter by 1
    attempts += 1

    # Calculate how many attempts are still available
    remaining = max_attempts - attempts

    # If attempts are still available, show the remaining count
    if remaining > 0:
        print(f"Incorrect password. Attempts remaining: {remaining}")

    # If no attempts are left, lock the account
    else:
        print("Account Locked")