# Luke Psyhogios, April 17th 2022, Section 001, Assignment 8, Problem #1: My Contacts

# Set conditional variables
valid_1 = False
valid_2 = False
valid_3 = False
test_1 = False
test_2 = True
test_3 = True
cond_1 = True
cond_2 = False
at = False
spaces = 0

# Set variables


# Get variables from user. Use while loop for data validation
while valid_1 == False:
    n_contact = int(input('How many contacts would you like to add? '))
    # If the user enters a number less than 1 for number of contacts they would like to add, try again
    if n_contact<1:
        print('Invalid, please try again')
    else:
        valid_1 = True
# Set lists
names = [' ']*n_contact
emails = [' ']*n_contact

for i in range(n_contact):
    # Use while loop for data validation
    while valid_2 == False:
        i = i+1
        i = str(i)
        # Ask user for contact name
        temp_name = input('Please enter the name of contact ' + i + ': ')
        i = int(i)
        i = i-1
        # If the name has two parts, it's valid
        for x in temp_name:
            if x == ' ':
                spaces += 1
            # If one of the characters is a number, the name is invalid
            try:
                x = int(x)
                test_1 = True                
            except:
                continue
        if spaces != 1 or test_1 == True:
            print('Invalid, please try again')
            valid_2 = False
            test_1 = False
            spaces = 0
        # If all conditions are met, store contact name in the names list
        else:
            names[i] = temp_name
            valid_2 = True
    valid_2 = False
    test_1 = False
    spaces = 0
    while valid_3 == False:
        i = i+1
        i = str(i)
        # Ask user for contact email
        temp_email = input('Please enter the email of contact ' + i + ': ')
        i = int(i)
        i = i-1
        string = temp_email[-1:-5:-1]
        for y in temp_email:
            if y == '@':
                # If there is one '@' in the email, it is valid
                at = True
                cond_2 = True
            if string != 'moc.':
                # If the email ends in .com, it is valid
                test_2 = False
            if cond_2 == True:
                try:
                    y = int(y)
                    test_3 = False                
                except:
                    continue
        if at == False or test_2 == False or test_3 == False:
            print('Invalid, please try again')
            valid_3 = False
            at = False
            test_2 = True
            test_3 = True
            cond_2 = False
        # Add email to email string if valid
        else:
            emails[i] = temp_email
            valid_3 = True
    valid_3 = False
    at = False
    test_2 = True
    test_3 = True
    cond_2 = False

# Display output
print('Thanks! Here is your address book:')

# Display contact book using a for loop
for i in range(n_contact):
    print('Name:', names[i], end=', ')
    print('Email:', emails[i])

            
                
            
            
                        
        
        
        
        
    

