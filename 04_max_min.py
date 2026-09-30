# 4. Find Maximum and Minimum Without max() / min()

"""
Write a program that finds the largest and smallest values in a list using loops only.
"""

# Create a list of numbers
numbers = [45, 12, 89, 23, 67, 5]

# Assume the first number is the largest initially
largest = numbers[0]

# Assume the first number is the smallest initially
smallest = numbers[0]

# Loop through the list starting from the second number
for number in numbers[1:]:

    # Check if the current number is greater than the largest number
    if number > largest:   
        # If yes, update largest with the current number
        largest = number

    # Check if the current number is smaller than the smallest number
    if number < smallest:
        # If yes, update smallest with the current number
        smallest = number

# Display the original list
print("Numbers:", numbers)

# Display the largest number
print("Largest:", largest)

# Display the smallest number
print("Smallest:", smallest)