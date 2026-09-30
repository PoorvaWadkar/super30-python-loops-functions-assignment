# 5. Character Frequency Counter

"""
Take a string from the user and calculate how many times each character occurs. 
Example: "banana" should identify the frequencies of b, a and n.
"""

# Take a string as input from the user
text = input("Enter a string: ")

# Create an empty dictionary to store each character and its frequency
frequency = {}

# Loop through each character in the string
for character in text:

    # Check if the character is already present as a key in the dictionary
    if character in frequency:

        # If it exists, increase its count by 1
        frequency[character] += 1

    else:
        # If it does not exist, add it to the dictionary with an initial count of 1
        frequency[character] = 1

# Print a heading
print("\nCharacter frequencies:")

# Loop through each key-value pair in the dictionary
for character, count in frequency.items():

    # Display the character and its frequency
    print(repr(character), ":", count)