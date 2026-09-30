# 2. Multiplication Table Generator

"""
Take a number from the user and print its multiplication table from 1 × N through 10 × N using a for loop. 
Then modify the program so the ending range can also be supplied by the user.
"""

# Take the number for which we want to generate the table
number = int(input("Enter a number: "))

# Display the heading of the multiplication table
print(f"\nMultiplication table of {number}")

# Loop through the multipliers from 1 to the value of 'end'
for multiplier in range(1, 11):

    # Calculate multiplier * number and display the result
    print(f"{multiplier} x {number} = {multiplier * number}")