# 20 . Student Registration System

"""
Build a menu-driven application using functions + for loops + while loops. 
The system should allow users to add a student, view all students, search by ID, update student details, delete a student, 
calculate class average marks, display the highest-performing student, and exit Store the records using appropriate Python data structures.
"""

# Create an empty dictionary to store all student records
# Student ID will be the key
# Student details will be stored as a nested dictionary
students = {}

# Function to add a new student
def add_student():

    # Take the student ID from the user
    student_id = input("Enter student ID: ").strip()

    # Check whether the student ID already exists
    if student_id in students:
        print("Student ID already exists.")
        return

    # Take the student's name
    name = input("Enter student name: ").strip()

    # Take the student's course
    course = input("Enter course: ").strip()

    try:
        # Take marks from the user and convert them to float
        marks = float(input("Enter marks: "))

        # Check whether marks are between 0 and 100
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    # Handle invalid input such as letters
    except ValueError:
        print("Enter a valid mark.")
        return

    # Add the student record to the students dictionary
    students[student_id] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    # Display success message
    print("Student added successfully.")


# Function to display all registered students
def view_students():

    # Check whether there are no student records
    if not students:
        print("No students registered.")
        return

    # Display a heading
    print("\n--- ALL STUDENTS ---")

    # Loop through student ID and student details
    for student_id, student in students.items():

        # Display the details of each student
        print(
            f"ID: {student_id} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']} | "
            f"Marks: {student['marks']}"
        )


# Function to search for a student using student ID
def search_student():

    # Ask the user for the student ID
    student_id = input("Enter student ID to search: ").strip()

    # Check whether the ID exists in the students dictionary
    if student_id in students:

        # Get the student details using the ID
        student = students[student_id]

        # Display the student's details
        print(
            f"ID: {student_id}\n"
            f"Name: {student['name']}\n"
            f"Course: {student['course']}\n"
            f"Marks: {student['marks']}"
        )

    # If the ID does not exist
    else:
        print("Student not found.")


# Function to update student details
def update_student():

    # Ask the user for the student ID
    student_id = input("Enter student ID to update: ").strip()

    # Check whether the student ID exists
    if student_id not in students:
        print("Student not found.")
        return

    # Get the student's existing details
    student = students[student_id]

    # Ask for new details
    # Existing values are shown inside [ ]
    new_name = input(f"Enter new name [{student['name']}]: ").strip()
    new_course = input(f"Enter new course [{student['course']}]: ").strip()
    new_marks = input(f"Enter new marks [{student['marks']}]: ").strip()

    # Update name only if the user entered a new name
    if new_name:
        student["name"] = new_name

    # Update course only if the user entered a new course
    if new_course:
        student["course"] = new_course

    # Update marks only if the user entered a new value
    if new_marks:

        try:
            # Convert the new marks to float
            marks = float(new_marks)

            # Check whether the marks are between 0 and 100
            if 0 <= marks <= 100:
                student["marks"] = marks

            else:
                print("Marks must be between 0 and 100. Marks not updated.")

        # Handle invalid marks such as letters
        except ValueError:
            print("Invalid marks. Marks not updated.")

    # Display update message
    print("Student details updated.")


# Function to delete a student
def delete_student():

    # Ask the user for the student ID
    student_id = input("Enter student ID to delete: ").strip()

    # Check whether the ID exists
    if student_id in students:

        # Delete the student record
        del students[student_id]

        print("Student deleted.")

    # If the ID does not exist
    else:
        print("Student not found.")


# Function to calculate the class average
def class_average():

    # Check whether there are no students
    if not students:
        print("No student records available.")
        return

    # Variable to store the total marks
    total = 0

    # Loop through all student records
    for student in students.values():

        # Add each student's marks to total
        total += student["marks"]

    # Calculate average marks
    average = total / len(students)

    # Display the average with 2 decimal places
    print(f"Class average marks: {average:.2f}")


# Function to find the student with the highest marks
def highest_performing_student():

    # Check whether there are no students
    if not students:
        print("No student records available.")
        return

    # Store the ID of the highest-scoring student
    highest_id = None

    # Start with -1 so that even 0 marks can become the highest
    highest_marks = -1

    # Loop through student ID and student details
    for student_id, student in students.items():

        # Check whether current student's marks are higher
        if student["marks"] > highest_marks:

            # Update the highest marks
            highest_marks = student["marks"]

            # Store the corresponding student ID
            highest_id = student_id

    # Get the details of the highest-performing student
    student = students[highest_id]

    # Display the student's details
    print("\n--- HIGHEST-PERFORMING STUDENT ---")
    print("ID:", highest_id)
    print("Name:", student["name"])
    print("Course:", student["course"])
    print("Marks:", student["marks"])


# Keep showing the menu until the user chooses Exit
while True:

    # Display the main menu
    print("\n===== STUDENT REGISTRATION SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Class Average")
    print("7. Display Highest-Performing Student")
    print("8. Exit")

    # Take the user's menu choice
    choice = input("Enter your choice: ")

    # Option 1: Add a student
    if choice == "1":
        add_student()

    # Option 2: View all students
    elif choice == "2":
        view_students()

    # Option 3: Search for a student
    elif choice == "3":
        search_student()

    # Option 4: Update student details
    elif choice == "4":
        update_student()

    # Option 5: Delete a student
    elif choice == "5":
        delete_student()

    # Option 6: Calculate class average
    elif choice == "6":
        class_average()

    # Option 7: Find highest-performing student
    elif choice == "7":
        highest_performing_student()

    # Option 8: Exit the program
    elif choice == "8":
        print("Exiting Student Registration System.")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please try again.")