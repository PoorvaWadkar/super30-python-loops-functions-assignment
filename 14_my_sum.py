# 14. Create Your Own sum() Function

"""
Write a function as def my_sum(numbers)
It should accept a list of numbers and return their sum without using Python's built-in sum().
"""

# Define a function named my_sum
def my_sum(numbers):

    # Start the total from 0
    total = 0

    # Go through each number in the list
    for number in numbers:

        # Add the current number to the total
        total += number

    # Return the final total to the place where the function was called
    return total


# Create a list of numbers
numbers = [10, 20, 30, 40]

# Call the my_sum function and pass the numbers list to it
# Store the returned result in the result variable
result = my_sum(numbers)

# Display the original list
print("Numbers:", numbers)

# Display the calculated sum
print("My sum:", result)