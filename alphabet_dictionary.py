# Luke Psyhogios, May 2nd 2022, Section 001, Assignment 10, Problem #0: Alphabet Dictionary
# function: cleanup_string
# input: a string to clean up
# processing: (1) makes the entire string lowercase.
# (2) retains only alphabetic and numeric characters
# all punctuation, spaces, and special characters removed]
# output: returns the cleaned up string
def cleanup_string(string):
    # Make string lowercase
    string = string.lower()
    # Create empty list
    list = [] 
    # If character is a number or letter, add it to the empty string
    for char in string:
        if char.isalpha() == True:
            list += char
        elif char.isnumeric() == True:
            list += char
        else:
            continue
    # Return the correct phrase
    return ''.join(list)

# Get user input
phrase = input('Enter a phrase: ')
phrase = cleanup_string(phrase)
dictionary = {}

# Add keys to the dictionary 
for char in phrase:
    # Add values to the dictionary
    if char in dictionary.keys():
        dictionary[char] += 1
    else:
        dictionary[char] = 1

# Sort the dictionary
dictionary = sorted(dictionary.items()) 

# Display output     
print('Report in ascending order by ASCII value:')
for k, v in dictionary:
    print(k, v)
