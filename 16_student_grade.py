# 16. Student Grade Function

"""
Create a function that accepts marks for five subjects, calculates total and percentage 
and returns a grade based on rules you define such as A, B, C, D or Fail. 
Add appropriate validation for invalid marks.
"""

# Define a function to calculate total, percentage and grade
def calculate_grade(marks):

    # Check whether exactly 5 subject marks are provided
    if len(marks) != 5:
        raise ValueError("Exactly five subject marks are required.")

    # Check each mark in the list
    for mark in marks:

        # Marks must be between 0 and 100
        if mark < 0 or mark > 100:
            raise ValueError("Each mark must be between 0 and 100.")

    # Calculate the total marks
    total = sum(marks)

    # Calculate the percentage
    percentage = total / 5

    # Decide the grade based on the percentage
    if percentage >= 90:
        grade = "A"

    elif percentage >= 75:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 40:
        grade = "D"

    else:
        grade = "Fail"

    # Return the total, percentage, and grade
    return total, percentage, grade


# try block is used to handle possible errors
try:

    # Create an empty list to store marks
    marks = []

    # Take marks for 5 subjects
    for subject in range(1, 6):

        # Ask the user to enter marks for each subject
        mark = float(input(f"Enter marks for subject {subject}: "))

        # Add the mark to the marks list
        marks.append(mark)

    # Call the calculate_grade function
    total, percentage, grade = calculate_grade(marks)

    # Display the results
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


# Catch ValueError if invalid input occurs
except ValueError as error:

    # Display the error message
    print("Invalid input:", error)