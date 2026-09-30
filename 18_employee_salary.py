# 18. Employee Salary Calculator

"""
Create a function that accepts employee name, basic salary, bonus percentage and tax percentage. 
Calculate gross salary, tax amount and final salary. Process at least five employees using a loop.
"""

# Define a function to calculate an employee's salary
def calculate_salary(name, basic_salary, bonus_percentage, tax_percentage):

    # Calculate the bonus amount
    bonus = basic_salary * (bonus_percentage / 100)

    # Add the bonus to the basic salary to calculate the gross salary
    gross_salary = basic_salary + bonus

    # Calculate the tax amount based on the gross salary
    tax_amount = gross_salary * (tax_percentage / 100)

    # Subtract the tax from the gross salary to calculate the final salary
    final_salary = gross_salary - tax_amount

    # Return the salary details as a dictionary
    return {
        "name": name,
        "gross_salary": gross_salary,
        "tax_amount": tax_amount,
        "final_salary": final_salary
    }


# Create a list containing employee information
employees = [
    ("Siya", 50000, 10, 5),
    ("Diya", 45000, 8, 4),
    ("Rohan", 60000, 12, 7),
    ("Meera", 55000, 10, 6),
    ("Kabir", 40000, 5, 3),
]


# Loop through each employee in the employees list
for employee in employees:

    # Call the calculate_salary function
    # *employee unpacks the tuple into separate arguments
    result = calculate_salary(*employee)

    # Display the employee's name
    print(f"\nEmployee: {result['name']}")

    # Display the gross salary with 2 decimal places
    print(f"Gross salary: ₹{result['gross_salary']:.2f}")

    # Display the tax amount with 2 decimal places
    print(f"Tax amount: ₹{result['tax_amount']:.2f}")

    # Display the final salary with 2 decimal places
    print(f"Final salary: ₹{result['final_salary']:.2f}")