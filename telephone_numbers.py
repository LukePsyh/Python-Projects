# Luke Psyhogios, March 28th 2022, Section 001, Assignment 7, Problem #1: Telephone Numbers

# Set conditional variable
valid = False

while valid == False:
    # Ask user to input their phone number
    number = str(input('What is your phone number? '))
    # Ensure phone number is not shorter than 11 digits...
    if len(number) < 11:
        print('Phone number is too short, please try again!')
        continue
    # ... nor longer
    if len(number) > 11:
        print('Phone number is too long, please try again!')
        continue
    # Manipulate input string into the proper format
    number = str('+' + number[0] + ' (' + number[1:4] + ') ' + number[4:7] + '-' + number[7:11] + '.')
    # Display output
    print('Your phone number is', number)
    valid = True
