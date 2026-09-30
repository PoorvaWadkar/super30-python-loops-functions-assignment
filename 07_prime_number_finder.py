# 7. Prime Number Finder

"""
Ask the user for a starting and ending number. Print all prime numbers within that 
range using nested loops.
"""

# Take the starting number from the user
start = int(input("Enter starting number: "))

# Take the ending number from the user
end = int(input("Enter ending number: "))

# Display a heading
print("Prime numbers:")

# Loop through all numbers from start to end
for number in range(max(2, start), end + 1):

    # Initially assume that the number is prime
    is_prime = True

    # Check possible divisors from 2 up to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):

        # If the number is exactly divisible by the divisor, then it is not a prime number
        if number % divisor == 0:

            # Mark the number as not prime
            is_prime = False

            # Stop checking further divisors
            break

    # If the number is still marked as prime, print it
    if is_prime:
        print(number, end=" ")

# Move to the next line after printing all prime numbers
print()