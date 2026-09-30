# 17. Shopping Cart using Functions

"""
Create functions for add_item(), remove_item(), view_cart(), calculate_total() and checkout(). 
Keep the application running using a while loop until checkout or exit.
"""

# Create an empty list to store all cart items
cart = []

# Function to add an item to the cart
def add_item():

    # Ask the user for the item name
    name = input("Enter item name: ").strip()

    # Try to convert price and quantity into the correct data types
    try:
        # Take the item price and convert it to a float
        price = float(input("Enter item price: "))

        # Take the quantity and convert it to an integer
        quantity = int(input("Enter quantity: "))

    # Handle invalid price or quantity input
    except ValueError:
        print("Please enter valid price and quantity.")

        # Stop this function
        return

    # Validate the item details
    # Name should not be empty
    # Price cannot be negative
    # Quantity must be greater than zero
    if not name or price < 0 or quantity <= 0:
        print("Invalid item details.")

        # Stop this function
        return

    # Add the item as a dictionary to the cart list
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    # Confirm that the item was added
    print("Item added.")


# Function to remove an item from the cart
def remove_item():

    # Check whether the cart is empty
    if not cart:
        print("Cart is empty.")

        # Stop this function
        return

    # Display the items in the cart
    view_cart()

    # Try to get the item number from the user
    try:
        # Convert the entered item number into an integer
        item_number = int(input("Enter item number to remove: "))

        # Remove the selected item from the list
        # User sees item numbers starting from 1, but Python list indexes start from 0
        removed = cart.pop(item_number - 1)

        # Display the name of the removed item
        print(f"Removed {removed['name']}.")

    # Handle invalid input or invalid item number
    except (ValueError, IndexError):
        print("Invalid item number.")


# Function to display all items in the cart
def view_cart():

    # Check whether the cart is empty
    if not cart:
        print("Cart is empty.")

        # Stop this function
        return

    # Display the cart heading
    print("\n--- CART ---")

    # Loop through every item in the cart
    # enumerate() provides both the index and the item
    # start=1 makes the displayed item number start from 1
    for index, item in enumerate(cart, start=1):

        # Calculate the total price for this particular item
        item_total = item["price"] * item["quantity"]

        # Display item number, name, price, quantity, and item total
        print(
            f"{index}. {item['name']} | "
            f"₹{item['price']:.2f} x {item['quantity']} = "
            f"₹{item_total:.2f}"
        )


# Function to calculate the total cost of all items
def calculate_total():

    # Start the total from zero
    total = 0

    # Go through every item in the cart
    for item in cart:

        # Add price × quantity to the total
        total += item["price"] * item["quantity"]

    # Return the final cart total
    return total


# Function to perform checkout
def checkout():

    # Check whether there are any items in the cart
    if not cart:
        print("Cart is empty. Nothing to checkout.")

        # Return False because checkout cannot happen
        return False

    # Display the cart before checkout
    view_cart()

    # Calculate the total amount
    total = calculate_total()

    # Display the total amount with 2 decimal places
    print(f"Total amount: ₹{total:.2f}")

    # Confirm checkout
    print("Checkout completed.")

    # Return True because checkout was successful
    return True


# Keep displaying the menu until the user exits or completes checkout
while True:

    # Display the shopping cart menu
    print("\n--- SHOPPING CART MENU ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")

    # Ask the user to select an option
    choice = input("Enter your choice: ")

    # Option 1: Add an item
    if choice == "1":
        add_item()

    # Option 2: Remove an item
    elif choice == "2":
        remove_item()

    # Option 3: View the cart
    elif choice == "3":
        view_cart()

    # Option 4: Calculate and display the cart total
    elif choice == "4":
        print(f"Cart total: ₹{calculate_total():.2f}")

    # Option 5: Checkout
    elif choice == "5":

        # checkout() returns True if checkout is successful
        if checkout():

            # Stop the while loop after successful checkout
            break

    # Option 6: Exit without checkout
    elif choice == "6":
        print("Exiting without checkout.")

        # Stop the while loop
        break

    # Handle an invalid menu choice
    else:
        print("Invalid choice.")