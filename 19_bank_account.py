# 19. Bank Account Mini Application

"""
Create functions for deposit(), withdraw(), check_balance() and transaction_history(). 
Use a while loop to keep the banking application running. Prevent withdrawals when sufficient balance is unavailable.
"""

# Store the current bank balance
balance = 0.0

# Store all deposit and withdrawal transactions
history = []

# Function to deposit money
def deposit(amount):
    # Use the global balance variable inside this function
    global balance

    # Check whether the deposit amount is valid
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    # Add the deposit amount to the balance
    balance += amount

    # Add the transaction details to the history list
    history.append(f"Deposited ₹{amount:.2f}")

    # Display success message
    print("Deposit successful.")


# Function to withdraw money
def withdraw(amount):
    # Use the global balance variable inside this function
    global balance

    # Check whether the withdrawal amount is valid
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")

    # Check whether enough balance is available
    elif amount > balance:
        print("Insufficient balance.")

    else:
        # Subtract the withdrawal amount from the balance
        balance -= amount

        # Add the withdrawal details to the history list
        history.append(f"Withdrew ₹{amount:.2f}")

        # Display success message
        print("Withdrawal successful.")


# Function to display the current balance
def check_balance():
    print(f"Current balance: ₹{balance:.2f}")


# Function to display transaction history
def transaction_history():

    # Check whether there are no transactions
    if not history:
        print("No transactions yet.")
        return

    # Display a heading
    print("\n--- TRANSACTION HISTORY ---")

    # Loop through each transaction in the history list
    for transaction in history:
        print(transaction)


# Keep displaying the bank menu until the user chooses Exit
while True:

    # Display the bank menu
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    # Take the user's menu choice
    choice = input("Enter your choice: ")


    # If the user selects Deposit
    if choice == "1":
        try:
            # Take the deposit amount and convert it to float
            amount = float(input("Enter deposit amount: "))

            # Call the deposit function
            deposit(amount)

        # Handle invalid input such as letters
        except ValueError:
            print("Enter a valid amount.")


    # If the user selects Withdraw
    elif choice == "2":
        try:
            # Take the withdrawal amount and convert it to float
            amount = float(input("Enter withdrawal amount: "))

            # Call the withdraw function
            withdraw(amount)

        # Handle invalid input such as letters
        except ValueError:
            print("Enter a valid amount.")


    # If the user selects Check Balance
    elif choice == "3":
        check_balance()


    # If the user selects Transaction History
    elif choice == "4":
        transaction_history()


    # If the user selects Exit
    elif choice == "5":
        print("Thank you for using the bank application.")

        # Stop the while loop
        break


    # If the user enters anything other than 1-5
    else:
        print("Invalid choice.")