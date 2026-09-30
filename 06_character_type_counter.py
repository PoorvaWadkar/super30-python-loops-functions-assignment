# 6. Vowel, Consonant, Digit, Space and Special Characters

"""
Create a program that analyzes a sentence and counts vowels, consonants, digits, spaces 
and special characters separately.
"""

# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Initialize counters for each type of character
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

# Go through each character in the sentence
for character in sentence:

    # Check whether the character is a letter
    if character.isalpha():

        # Convert the character to lowercase and check whether it is one of the vowels
        if character.lower() in "aeiou":
            vowels += 1

        # If it is a letter but not a vowel, it is a consonant
        else:
            consonants += 1

    # Check whether the character is a digit (0-9)
    elif character.isdigit():
        digits += 1

    # Check whether the character is a whitespace character
    elif character.isspace():
        spaces += 1

    # If it is none of the above, count it as a special character
    else:
        special_characters += 1

# Display the final counts
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)