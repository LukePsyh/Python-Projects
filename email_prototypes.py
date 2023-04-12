# Luke Psyhogios, April 25th 2022, Section 001, Assignment 7, Problem #1: Email Prototype
# Set conditional variable
valid = True
valid_2 = True


# Import Functions
from PsyhogiosLuke_assignment9_problem1_functions import valid_username
from PsyhogiosLuke_assignment9_problem1_functions import valid_password
from PsyhogiosLuke_assignment9_problem1_functions import username_exists
from PsyhogiosLuke_assignment9_problem1_functions import add_user
from PsyhogiosLuke_assignment9_problem1_functions import delete_messages
from PsyhogiosLuke_assignment9_problem1_functions import print_messages
from PsyhogiosLuke_assignment9_problem1_functions import send_message
import os
wd = os.getcwd()
path = wd + '/'

# Read the data stored in the file
user_info_file = open(path+'user_info.txt', 'r')
user_data = user_info_file.read()
user_info_file.close()

# Split the data into 
user_data = user_data.split('\n')
usernames = []
passwords = []
for i in user_data:
    try:       
        data = i.split(',')
        usernames.append(data[0])
        passwords.append(data[1])
    except:
        break

while '' in usernames:
    usernames.remove('')


while valid == True:
    # Set conditional variable
    valid_2 = True
    # Get user input
    choice = str(input('(l)ogin, (r)egister or (q)uit: '))
    print('\n')
    # If user opts to register
    if choice == 'r':
        print('Register for an account')
        new_username = str(input('Username (case sensitive): '))
        new_password = str(input('Password (case sensitive): '))
        # If username or password is invalid, continue the loop
        if valid_username(new_username) == False:
            print('Username is invalid, registration cancelled')
            print('\n')
            continue
        elif valid_password(new_password) == False:
            print('Password is invalid, registration cancelled')
            print('\n')
            continue
        # If username already exists, continue the loop
        elif username_exists(new_username) == True:
            print('Duplicate username, registration cancelled')
            print('\n')
            continue
        elif new_username in usernames:
            print('Duplicate username, registration cancelled')
            print('\n')
            continue
        # If everything is okay, add the new user to the database
        else:
            add_user(new_username, new_password)
            print('Registration successful!')
            print('\n')
            usernames.append(new_username)
            passwords.append(new_password)
        continue
    elif choice == 'l':
        print('Login')
        username = str(input('Username (case sensitive): '))
        password = str(input('Password (case sensitive): '))
        try:
            username_index = usernames.index(username)
        # Username/password won't exist if there is an error getting the index
        except:
            print('Username does not exist, login cancelled')
            continue
        try:
            password_index = passwords.index(password)
        except:
            print('Password does not exist, login cancelled')
            continue
        if username_index == password_index:
            while valid_2 == True:         
                print('You have been logged in succesfully as', username)
                second_answer = str(input('(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: '))
                if second_answer == 'r':
                    print('\n')
                    print_messages(username)
                    print('\n')
                    continue
                elif second_answer == 's':
                    recipient = str(input('Username of recipient: '))
                    # Ensure the recipient is a real user
                    if recipient not in usernames:
                        print('Unknown recipient')
                        print('\n')
                        continue
                    message_recipient = str(input('Type your message: '))
                    send_message(username, recipient, message_recipient)
                    print('Message sent!')
                    print('\n')
                    continue
                elif second_answer == 'd':
                    delete_messages(username)
                    print('Your messages have been deleted')
                    print('\n')
                elif second_answer == 'l':
                  print('Logging out as username', username)
                  print('\n')
                  valid_2 = False
                else:
                    print('Invalid choice')
                    continue
        # If the index' don't align, the username/password combo is incorrect
        else:
            print('Incorrect username or password. Login cancelled')
            continue
    elif choice == 'q':
        print('\n')
        print('Goodbye!')
        valid = False
        break
    # If the initial input is something non-valid
    else:
        print('Invalid option. Try again.')
        
    
                 
