# Luke Psyhogios, April 25th 2022, Section 001, Assignment 7, Problem #1: Email Prototype
usernames = []
passwords = []
# function: valid_username
# input: a username (string)
# processing: determines if the username supplied is valid. for the purpose
# of this program a valid username is defined as follows:
# (1) must be 5 characters or longer
# (2) must be alphanumeric (only letters or numbers)
# (3) the first character cannot be a number
# output: boolean (True if valid, False if invalid)


# function: valid_username
# input: a username (string)
# processing: determines if the username supplied is valid. for the purpose
# of this program a valid username is defined as follows:
# (1) must be 5 characters or longer
# (2) must be alphanumeric (only letters or numbers)
# (3) the first character cannot be a number
# output: boolean (True if valid, False if invalid)
def valid_username(username):
    # Create empty lists
    lower = []
    upper = []
    numbers = []
    # Populate lists with data
    for i in range(97, 123):
        lower += chr(i)
    for i in range(65, 91):
        upper += chr(i)
    for i in range(48, 57):
        numbers += chr(i)
    # Convert username into a string
    username = str(username)
    # Set conditional variable
    valid = True
    # Make sure length exceeds or is equal to 5
    if len(username)<5:
        valid = False
        return valid
    # If a character is not a number or letter the username is invalid
    for character in username:
        if character in lower:
            x = 5
        elif character in upper:
            x = 5
        elif character in numbers:
            x = 5
        else:
            valid = False
            return valid
    # The first character of the username must be a number
    if username[0] in upper:
        x = 5
    if username[0] in lower:
        x = 5
    else:
        valid = False
        return valid
    return valid


# function: valid_password
# input: a password (string)
# processing: determines if the password supplied is valid. for the purpose
# of this program a valid password is defined as follows:
# (1) must be 5 characters or longer
# (2) must be alphanumeric (only letters or numbers)
# (3) must contain at least one lowercase letter
# (4) must contain at least one uppercase letter
# (5) must contain at least one number
# output: boolean (True if valid, False if invalid)
def valid_password(password):
    # Create empty lists
    lower = []
    upper = []
    numbers = []
    # Populate lists with data
    for i in range(97, 123):
        lower += chr(i)
    for i in range(65, 91):
        upper += chr(i)
    for i in range(48, 57):
        numbers += chr(i)
    # Convert password into a string
    password = str(password)
    # Set variables
    valid = True
    lower_n = 0
    upper_n = 0
    number_n = 0
    # Make sure length exceeds or is equal to 5
    if len(password)<5:
        valid = False
        return valid
    # If a character is not a number or letter the password is invalid
    for character in password:
        if character in lower:
            # Keep track of the number of letters and numbers
            lower_n += 1
        elif character in upper:
            upper_n += 1
        elif character in numbers:
            number_n += 1
        else:
            valid = False
            return valid
    # Make sure there is at least one uppercase number, lowercase number, and number in the password
    if lower_n<1 or upper_n<1 or number_n<1:
        valid = False
        return valid
    return valid

# function: username_exists
# input: a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output: boolean (True if found, False if not found)
def username_exists(username):
    username = str(username)
    # If the inputted username is in the usernames list, the username does exist
    if username in usernames:
        return True
    else:
        return False

# function: check_password
# input: a username (string) and a password (string)
# processing: determines if the username / password combination
# supplied matches one of the user accounts represented
# in the 'user_info.txt' file
# output: boolean (True if valid, False if invalid)
def check_password(username, password):
    username = str(username)
    password = str(password)
    # Use try incase the username or password doesn't exist
    # Get the index for the inputted username and password if they do exist
    try:
        username_index = usernames.index(username)
    except:
        return False
    try:
        password_index = passwords.index(password)
    except:
        return False
    # If the password and username exist at the same location, it is the right password so return True
    if password_index == username_index:
        return True
    else:
        return False

# function: add_user
# input: a username (string) and a password (string)
# processing: if the user being supplied is not already in the
# 'user_info.txt' file they should be added, along with
# their password.
# output: boolean (True if added successfully, False if not)
def add_user(username, password):
    username = str(username)
    password = str(password)
    # Ensure the username does not already exist
    if username_exists(username) == True:
        return False
    # Ensure username is valid
    if valid_username(username) == False:
        return False
    # Ensure password is valid  
    elif valid_password(password) == False:
        return False
    else:
        # Store new data in the user_info doc
        new_info = username + ',' + password + '\n'
        user_info_file = open('user_info.txt', 'a')
        user_info_file.write(new_info)
        user_info_file.close()
        # Send welcome message to new user
        import os
        import datetime
        d = datetime.datetime.now()
        month = str(d.month)
        day = str(d.day)
        year = str(d.year)
        hour = str(d.hour)
        minute = str(d.minute)
        second = str(d.second)
        string = username + '.txt'
        new_path = 'messages/' + string
        message = 'Admin|' + month + '/' + day + '/' + year + ' ' + hour + ':' + minute + ':' + second + '|Welcome to your account!' + '\n'
        empty_folder = open(new_path, 'w')
        empty_folder.write(message)
        empty_folder.close()
        return True

# function: send_message
# input: a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given
# users with the following information:
# sender|date_and_time|message\n
# output: nothing
import datetime
def send_message(sender, recipient, message):
    import os
    sender = str(sender)
    recipient = str(recipient)
    message = str(message)
    string = recipient + '.txt'
    new_path = 'messages/' + string
    d = datetime.datetime.now()
    month = str(d.month)
    day = str(d.day)
    year = str(d.year)
    hour = str(d.hour)
    minute = str(d.minute)
    second = str(d.second)
    message = sender + '|' + month + '/' + day + '/' + year + ' ' + hour + ':' + minute + ':' + second + '|' + message + '\n' 
    try:
        # Read file to ensure it exists
        file_two = open(new_path, 'r')
        file_two.close()
        # Add message to recipient's file
        file = open('messages/' + string, 'a')
        file.write(message)
        file.close()
    except:
        # If file cannot be opened, the user does not exist
        print("Recipient doesn't exist")

# function: print_messages
# input: a username (string)
# processing: prints all messages sent to the username in question. assume you have this file named 'pikachu.txt':
# output: no return value (simply prints the messages)
def print_messages(username):
    import os
    message_n = 0
    string_two = username + '.txt'
    newer_path = 'messages/' + string_two
    # Get messages from the proper file
    mess = open(newer_path, 'r')
    message_data = mess.read()
    mess.close()
    messages = message_data.split('\n')
    length = len(message_data)
    if length<2:
        print('No messages in your inbox')
    for message in messages:
        message_n += 1
        # Display all messages
        part = message.split('|')
        try:
            part[2]
            print('Message #', message_n, ' recieved from ', part[0], sep='')
            print('Time:', part[1])
            print(part[2])
            print('\n')
        except IndexError:
            break
        

# function: delete_messages
# input: a username (string)
# processing: erases all data in the messages file for this user
# output: no return value
def delete_messages(username):
    import os
    string = username + '.txt'
    new_path = 'messages/' + string
    file_to_delete = open(new_path, 'w')
    file_to_delete.close()
    

