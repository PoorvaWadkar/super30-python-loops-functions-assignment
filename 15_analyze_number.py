# 15. Reusable Number Analysis Function

"""
Create a function as def analyze_number(number): ...
It should determine whether the number is positive/negative/zero, even/odd and 
prime/not prime. Return the results rather than only printing them.
"""

# Define a function to check whether a number is prime
def is_prime(number):

    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check possible divisors from 2 up to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):

        # If the number is exactly divisible by the divisor then the number is not prime
        if number % divisor == 0:
            return False

    # If no divisor was found, the number is prime
    return True


# Define a function to analyze a number
def analyze_number(number):

    # Check whether the number is positive, negative, or zero
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Check whether the number is even or odd
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    # Check whether the number is prime
    # is_prime(number) returns True or False
    # The conditional expression converts it into a readable result
    prime_status = "Prime" if is_prime(number) else "Not Prime"

    # Return all the analysis results as a dictionary
    return {
        "sign": sign,
        "parity": parity,
        "prime_status": prime_status
    }


# Take a number from the user
number = int(input("Enter a number: "))

# Call the analyze_number function
result = analyze_number(number)

# Display the analysis result
print("Analysis:", result)