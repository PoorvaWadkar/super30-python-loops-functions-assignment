# 10. ATM Withdrawal Simulator using while

"""
Start with a balance of ₹10,000. Continuously show the user options to check balance, deposit money, 
withdraw money or exit. The program should continue until the user explicitly chooses Exit.
"""

# Set the initial account balance
balance = 10000.0

# Keep showing the ATM menu until the user chooses Exit
while True:

    # Display the ATM menu
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Ask the user to select an option
    choice = input("Enter your choice: ")

    # Option 1: Check the current balance
    if choice == "1":
        print(f"Current balance: ₹{balance:.2f}")

    # Option 2: Deposit money
    elif choice == "2":

        # Ask the user for the deposit amount
        amount = float(input("Enter deposit amount: "))

        # Make sure the deposit amount is greater than zero
        if amount > 0:

            # Add the deposit amount to the balance
            balance += amount

            # Display the updated deposit amount
            print(f"₹{amount:.2f} deposited successfully.")

        else:
            print("Deposit amount must be greater than zero.")

    # Option 3: Withdraw money
    elif choice == "3":

        # Ask the user for the withdrawal amount
        amount = float(input("Enter withdrawal amount: "))

        # Check whether the withdrawal amount is valid
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")

        # Check whether there is enough balance
        elif amount > balance:
            print("Insufficient balance.")

        # If the amount is valid and balance is sufficient
        else:

            # Subtract the withdrawal amount from the balance
            balance -= amount

            # Display the withdrawn amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    # Option 4: Exit the ATM
    elif choice == "4":
        print("Thank you for using the ATM.")

        # Stop the while loop
        break

    # Handle any invalid menu choice
    else:
        print("Invalid choice. Please try again.")