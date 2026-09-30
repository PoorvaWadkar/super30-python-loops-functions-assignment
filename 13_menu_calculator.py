# 13. Menu-Driven Calculator

"""
Build a continuously running calculator using while. Provide Addition, Subtraction, Multiplication, 
Division, Modulus and Exit operations. Handle division by zero properly.
"""

# Keep displaying the calculator menu until the user chooses Exit
while True:

    # Display the calculator menu
    print("\n--- CALCULATOR ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    # Ask the user to select an operation
    choice = input("Enter your choice: ")

    # If the user chooses 6, close the calculator
    if choice == "6":
        print("Calculator closed.")

        # Stop the while loop
        break

    # Check whether the choice is a valid calculator option
    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid choice.")

        # Skip the remaining code and start the next loop iteration
        continue

    # Take the first number from the user
    first = float(input("Enter first number: "))

    # Take the second number from the user
    second = float(input("Enter second number: "))

    # Perform addition
    if choice == "1":
        print("Result:", first + second)

    # Perform subtraction
    elif choice == "2":
        print("Result:", first - second)

    # Perform multiplication
    elif choice == "3":
        print("Result:", first * second)

    # Perform division
    elif choice == "4":

        # Check whether the second number is zero
        if second == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result:", first / second)

    # Perform modulus
    elif choice == "5":

        # Check whether the second number is zero
        if second == 0:
            print("Modulus by zero is not allowed.")
        else:
            print("Result:", first % second)