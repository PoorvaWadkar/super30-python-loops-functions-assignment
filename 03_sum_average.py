# 3. Sum and Average Without sum()

"""
Given a list of numbers, calculate the total and average using a loop. 
Do not use Python's built-in sum() function.
"""

# Create a list containing five numbers
numbers = [10, 20, 30, 40, 50]

# Initialize the total to 0
total = 0

# Loop through each number in the list
for number in numbers:

    # Add the current number to the total
    total += number  

# Calculate the average
average = total / len(numbers)

# Display the original list
print("Numbers:", numbers)

# Display the calculated total
print("Total:", total)

# Display the calculated average
print("Average:", average)

