# Luke Psyhogios, May 2nd 2022, Section 001, Assignment 10, Problem #2: Battleship
from random import randint
# Initial variables
valid_3 = True
valid_4 = True
valid_5 = True
valid_6 = True
valid_7 = True

# Create empty board using nested lists
user_board = [['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.']]

comp_board = [['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.']]

hidden_board = [['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.']]




# function: create_board
# input: list which you would like to be displayed
# output: displays the board which you called
def create_board(list):
    accumulator = 0
    board = ''
    value = 0
    for i in range(4):
        line = ''.join(list[i])
        if value != 0:
            board += '\n'
        board += line + '\n' + ('-' * 5)
        value += 1
    return print(board)


y = 1
# Ask user for ship locations
while valid_3 == True:
    valid_1 = True
    valid_2 = True
    while valid_1 == True:
        row_placement = int(input('Please enter a row: '))
        # Ensure the row is valid
        if row_placement>3 or row_placement<0:
            print('Invalid, try again!')
            continue
        else: 
            valid_1 = False
    while valid_2 == True:
        # Ensure the column is valid
        column_placement = int(input('Please enter a column: '))
        if column_placement>4 or column_placement<0:
            print('Invalid, try again!')
            continue
        else:
            valid_2 = False
    # Ensure the location has not already been selected
    if user_board[row_placement][column_placement] == 'S':
        print('Ship already exists in that location.')
        continue
    else:
        user_board[row_placement][column_placement] = 'S'
        print('Ship', y, 'placed.')
        y += 1
    if y == 6:
        valid_3 = False 
# Display user board
print('Here is your board:')
create_board(user_board)

z = 0
#  Create computer's board
while valid_4 == True:
    # Assign random row and column values
    comp_row = randint(1, 3)
    comp_column = randint(1,4)
    # Ensure that location has not already been hit
    if comp_board[comp_row][comp_column] == 'S':
        continue
    else:
        comp_board[comp_row][comp_column] = 'S'
        z += 1
    # After five ships have been placed, escape the loop
    if z == 5:
        valid_4 = False

# Display program
print("Let's play!")

# Set variables for display
go = 1
turn = -1
comp_ships = 5
user_ships = 5
# Display game
while valid_5 == True:
    valid_6 = True
    valid_7 = True
    go += 1
    turn += 1
    if go%2 == 0:
        print("User's turn...")
        while valid_6 == True:
            # Get user shot selection
            user_row_shot = int(input('Please enter a row: '))
            user_column_shot = int(input('Please enter a column: '))
            # Ensure this is the first time the user is attacking that spot
            if hidden_board[user_row_shot][user_column_shot] == 'X' or hidden_board[user_row_shot][user_column_shot] == 'O':
                print("You've already gone here, please try again.")
                continue
            else:
                valid_6 = False
        # If the user succesfully guesses where a ship it, it's a hit
        if comp_board[user_row_shot][user_column_shot] == 'S':
            print('Hit!')
            hidden_board[user_row_shot][user_column_shot] = 'X'
            print("Computer's board:")
            create_board(hidden_board)
            comp_ships -= 1
        # A miss
        else:
            print('Miss!')
            hidden_board[user_row_shot][user_column_shot] = 'O'
            print("Computer's board:")
            create_board(hidden_board)
        if comp_ships<1:
            print('User won in', turn, 'turns!')
            valid_5 = False
    else:
        print("Computer's turn...")
        while valid_7 == True:
            # Get random shot selection from the computer
            comp_row_shot = randint(1,3)
            comp_column_shot = randint(1,4)
            # Ensure this is the first time the computer is attacking this spot
            if user_board[comp_row_shot][comp_column_shot] == 'X' or user_board[comp_row_shot][comp_column_shot] == 'O':
                continue
            else:
                valid_7 = False
        # If the computer gets a hit
        if user_board[comp_row_shot][comp_column_shot] == 'S':
            print('Hit!')
            user_board[comp_row_shot][comp_column_shot] = 'X'
            print("User's board:")
            create_board(user_board)
            comp_ships -= 1
        # A miss
        else:
            print('Miss!')
            user_board[comp_row_shot][comp_column_shot] = 'O'
            print("User's board:")
            create_board(user_board)
        if user_ships<1:
            print('Computer won in', turn, 'turns!')
            valid_5 = False