# 9. Student Marks Analyzer

"""
Store marks of multiple students in a list. Using loops, calculate highest marks, lowest marks, 
average marks, number of students who passed and number who failed. Consider 40 as the passing mark.
"""

# Store the marks of students in a list
marks = [78, 35, 91, 62, 28, 84, 45, 39, 73, 56]

# Assume the first mark is initially the highest
highest = marks[0]

# Assume the first mark is initially the lowest
lowest = marks[0]

# Variable to store the total of all marks
total = 0

# Counter for students who passed
passed = 0

# Counter for students who failed
failed = 0

# Go through each mark in the list
for mark in marks:

    # Add the current mark to the total
    total += mark

    # Check if the current mark is higher than the current highest
    if mark > highest:
        highest = mark

    # Check if the current mark is lower than the current lowest
    if mark < lowest:
        lowest = mark

    # Check whether the student has passed
    # Passing mark is 40
    if mark >= 40:
        passed += 1
    else:
        failed += 1

# Calculate the average marks
average = total / len(marks)

# Display the results
print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students passed:", passed)
print("Students failed:", failed)