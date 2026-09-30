# 1. Number Analyzer using for loop

"""
Take a number N from the user. Print all numbers from 1 to N, identify whether each 
number is even or odd and finally display the total count of even and odd numbers.
"""

# Take a number from the user and convert it from string to integer
n = int(input("Enter a number N: "))

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through numbers from 1 to N
for number in range(1, n + 1):

    # Check if the number is divisible by 2
    if number % 2 == 0:
        print(number, "- Even")

        # Increase the even number counter by 1
        even_count += 1

    else:
        # If the number is not divisible by 2, it is odd
        print(number, "- Odd")

        # Increase the odd number counter by 1
        odd_count += 1

# Display the total number of even numbers
print("Total even numbers:", even_count)

# Display the total number of odd numbers
print("Total odd numbers:", odd_count)