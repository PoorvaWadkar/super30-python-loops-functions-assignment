# 8. Pattern Generator

"""
Using nested for loops, generate the following pattern for a user-supplied value of N:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# Take the number of rows from the user
n = int(input("Enter the number of rows: "))

# Outer loop controls the number of rows
for row in range(1, n + 1):

    # Inner loop prints numbers from 1 up to the current row number
    for number in range(1, row + 1):
        print(number, end=" ")

    # Move to the next line after printing one row
    print()