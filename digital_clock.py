# Luke Psyhogios, March 28th 2022, Section 001, Problem #2

# Import functions
import digitalclock
from digitalclock import print_number
from digitalclock import plus
from digitalclock import minus
from digitalclock import check_answer
from random import randint

# Set conditional variables
condition_1 = True
condition_2 = True
condition_3 = True

# Set program variables
correct = 0


# Begin data validation for user input
while condition_1 == True:
    # Ask user how many questions they would like to attempt
    n_questions = int(input('How many problems would you like to attempt? '))
    # Questions must be greater than 0
    if n_questions < 0:
        print('Invalid number, try again')
        print()
        continue
    # If n_questions is greater than 0, continue to question 2
    else:
        condition_1 = False
        while condition_2 == True:
            width = int(input('How wide do you want your digits to be? 5-10: '))
            # Width must be between 5 and 10
            if width > 10 or width < 5:
                print('Invalid width, try again')
                print()
                continue
            # If width is between 5 and 10, continue to question 3
            else:
                condition_2 = False
                while condition_3 == True:
                    character = str(input('What character would you like to use? '))
                    # Character must be a string with the length of one
                    if len(character) > 1:
                        print('String too long, try again')
                        print()
                        continue
                    if type(character) != str:
                        print('Not a string, try again')
                        print()
                        continue
                    # If all data is valid, escape while loop
                    else:
                        condition_3 = False
                        break
           
# Display program to user
print()
print('Here we go!')

# Use for loop for questions
for n in range(n_questions+1):
    if n == n_questions:
        break
    print()
    print('What is .....')
    # Get random numbers to display
    number1 = int(randint(1, 9))
    number2 = int(randint(1, 9))
    # Randomly assign '+' or '-' to character
    symbol = randint(1,2)
    # Assign and display '+'...  
    if symbol == 1:
        symbol = '+'
    # ... or '-' to character
    else:
        symbol = '-'
    # Display first number
    print_number(number1, width, character)
    print()
    if symbol == '+':
        print(plus(width, character))
    if symbol == '-':
        print(minus(width, character))
        print()
    # Display second number
    print_number(number2, width, character)
    print()
    # Get user answer
    number3 = int(input('='))
    # Evaluate whether user answer is correct or incorrect
    if check_answer(number1, number2, number3, symbol) == True:
        print('Correct!')
        # If user gets number correct, add one to their total
        correct += 1
    else:
        print("Sorry, that's not correct.")
    if n == n_questions:
        break



# Display test results
print()
print('You got', correct, 'out of', n_questions, 'correct!')

        
        
        
    
    
            
        
            
            
            
    
        
