# Luke Psyhogios, April 11th 2022, Section 001, Assignment 7, Problem #0: New User

# Set conditional variable
valid = False

while valid == False:
    # Get username from user
    username = input('Enter a username: ')
    # Set variables
    length = len(username)
    is_alnum = username.isalnum()
    digits = 0
    lower = 0
    upper = 0
    first_c = username[0].isdigit()
    last_c = username[length-1].isdigit()
    # Count how many digits and capital/lowercase letters there are
    for i in range(length):
        if username[i].isdigit():
            digits += 1
        elif username[i].isalpha():
            if username[i].isupper():
                upper += 1
            else:
                lower += 1
    # Display output
    print('* Length of username:', length)
    print('* All characters are alpha-numeric:', is_alnum)
    print('* First and last characters are not digits:', not(first_c or last_c))
    print('* # of uppercase characters in the username:', upper)
    print('* # of lowercase characters in the username:', lower)
    print('* # of digits in the username:', digits)
    # Determine whether username is valid or not
    if length >= 8 and length <= 15 and is_alnum == True and upper >= 1 and \
       lower >=1 and digits >= 1 and first_c == False and last_c == False:
        valid = True
    if valid == True:
        print('Username is valid!')
        break
    else:
        print('Username is invalid, please try again')
    print()
    print()
        
        
        
    
