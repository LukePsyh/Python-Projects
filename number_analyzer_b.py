# Luke Psyhogios, March 28th 2022, Section 001, Problem #1b: Number Analyzer (PROGRAM AFTER FUNCTION DEFINITIONS)
# function: is_even
# input: a positive integer
# processing: determines if the supplied number is even
# output: Boolean
def is_even(n):
    if n%2 == 0 and n>0:
        return True
    else:
        return False
# function: is_odd
# input: a positive integer
# processing: determines if the supplied number is odd
# output: Boolean
def is_odd(n):
    if n%2 != 0 and n>0:
        return True
    else:
        return False
    
# function: is_prime
# input: a positive integer
# processing: determines if the supplied number is prime. a prime number is
# a number that only has two factors - the number 1 and itself.
# for example, 17 is prime because it only has two factors (1 and
# 17). in order to determine this you might need to count # of
# factors between 1 and the number you are testing. a note on
# efficiency: if you are testing a number (say, 15) and you find a
# factor (say, 3) - do you need to even continue
# to find additional factors?
# output: Boolean
def is_prime(n):
    condition = True
    for x in range(2, n):
        if n%x == 0:
            condition = False
    if condition == True:
        return True
    if condition == False:
        return False

# function: is_perfect
# input: a positive integer
# processing: determines if the supplied number is perfect. a perfect number
# is a number that is equal to the sum of its factors (i.e. the
# number 6 is perfect because 6 = 1 + 2 + 3)
# output: Boolean
def is_perfect(n):
    condition = True
    counter = 0
    for x in range(1, n):
        if n%x == 0:
            counter += x
    if n == counter:
        return True
    else:
        return False
    
# function: is_abundant
# input: a positive integer
# processing: determines if the supplied number is abundant. an abundant #
# is a number that is less than the sum of its factors (i.e. the
# number 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
# note: this includes proper divisors only (12 itself is excluded)
# output: Boolean
def is_abundant(n):
    condition = True
    counter = 0
    for x in range(1, n):
        if n%x == 0:
            counter += x
    if n<counter:
        return True
    else:
        return False


# Program

# Set conditional variables
condition_1 = True




while condition_1 == True:
    # Display main menu
    print('Main Menu')
    print()
    print('1 - Find all prime numbers within a given range')
    print('2 - Find all perfect numbers within a given range')
    print('2 - Find all abundant numbers within a given range')
    print('4 - Chart all even, odd, prime, perfect and abundant numbers within a given range')
    print('5 - Quit')
    print()
    print()
    print()
    # Set conditional variables
    condition_2 = True
    condition_3 = True
    condition_4 = True
    condition_5 = True
    condition_6 = True
    condition_7 = True
    condition_8 = True
    condition_9 = True
    condition_10 = True
    # Validate that the choice is an integer
    while condition_2 == True:
        choice = int(input('Your choice: '))
        if type(choice) != int:
            print("I don't understand that ...")
            print()
            print()
            print()
        # Validate that the choice is between 1 and 5
        if choice>5 or choice<1:
            print("Invalid choice, try again")
            print()
            print()
            print()
        if choice == 1:
            while condition_3 == True:
                # Ask user to enter a starting number
                is_prime_n1 = int(input('Enter starting number (positive only): '))
                # If the number is negative prompt the user to enter another number
                if is_prime_n1<0:
                    print('Invalid, try again')
                else:
                    condition_3 = False
            # Ask user to enter an ending number
            while condition_4 == True:
                is_prime_n2 = int(input('Enter ending number: '))
                print()
                # Validate that the ending number is greater than the starting number
                if is_prime_n1>is_prime_n2:
                    print('Invalid, try again')
                else:
                    condition_4 = False
            # Display top of output
            print('All prime numbers between', is_prime_n1, 'and', is_prime_n2)
            print('#'*14)
            for x in range(is_prime_n1, is_prime_n2+1):
                # Print all prime numbers
                if is_prime(x) == True:
                    print(x)
            print('#'*14)
            print()
            print()
            condition_2 = False
        if choice == 2:
            while condition_5 == True:
                # Ask user to enter a starting number
                is_perfect_n1 = int(input('Enter starting number (positive only): '))
                # If the number is negative prompt the user to enter another number
                if is_perfect_n1<0:
                    print('Invalid, try again')
                else:
                    condition_5 = False
            # Ask user to enter an ending number
            while condition_6 == True:
                is_perfect_n2 = int(input('Enter ending number: '))
                print()
                # Validate that the ending number is greater than the starting number
                if is_perfect_n1>is_perfect_n2:
                    print('Invalid, try again')
                else:
                    condition_6 = False
            print('All perfect numbers between', is_perfect_n1, 'and', is_perfect_n2)
            print('#'*14)
            for x in range(is_perfect_n1, is_perfect_n2+1):
                # Print all perfect numbers
                if is_perfect(x) == True:
                    print(x)
            print('#'*14)
            print()
            print()
            condition_2 = False
        if choice == 3:
            while condition_7 == True:
                # Ask user to enter a starting number
                is_abundant_n1 = int(input('Enter starting number (positive only): '))
                # If the number is negative prompt the user to enter another number
                if is_abundant_n1<0:
                    print('Invalid, try again')
                else:
                    condition_7 = False
            # Ask user to enter an ending number
            while condition_8 == True:
                is_abundant_n2 = int(input('Enter ending number: '))
                print()
                # Validate that the ending number is greater than the starting number
                if is_abundant_n1>is_abundant_n2:
                    print('Invalid, try again')
                else:
                    condition_8 = False
            print('All abundant numbers between', is_abundant_n1, 'and', is_abundant_n2)
            print('#'*14)
            for x in range(is_abundant_n1, is_abundant_n2+1):
                # Print all prime numbers
                if is_abundant(x) == True:
                    print(x)
            print('#'*14)
            print()
            print()
            condition_2 = False
        if choice == 4:
             while condition_9 == True:
                # Ask user to enter a starting number
                is_all_n1 = int(input('Enter starting number (positive only): '))
                # If the number is negative prompt the user to enter another number
                if is_all_n1<0:
                    print('Invalid, try again')
                else:
                    condition_9 = False
             while condition_10 == True:
                is_all_n2 = int(input('Enter ending number: '))
                print()
                # Validate that the ending number is greater than the starting number
                if is_all_n1>is_all_n2:
                    print('Invalid, try again')
                else:
                    condition_10 = False
                # Format the top of the columns for display
                number = format('Number', '<10s')
                even = format('Even', '<10s')
                odd = format('Odd', '<10s')
                prime = format('Prime', '<10s')
                perfect = format('Perfect', '<10s')
                abundant = format('Abundant', '<10s')
                # Display the top of the columns
                print(number, even, odd, prime, perfect, abundant)
                for x in range(is_all_n1, is_all_n2+1):
                    print()
                    x = str(x)
                    # Display the 'Number' column information
                    formatted_x = format(x, '<2s')
                    print(formatted_x, end='')
                    # Set variables for display and functions
                    x = int(x)
                    spaces = format('', '<2s')
                    for i in range(0,6):
                        # Print an x is the given function is True and the loop is in the iteration that matches up with 'i'
                        if i == 1 and is_even(x) == True:
                            print(' x', end='')
                        # Print spaces inbetween x's
                        print(spaces, end='')
                        if i == 2 and is_odd(x) == True:
                            print('  x', end='')
                        print(spaces, end='')
                        if i == 3 and is_prime(x) == True:
                            print('x', end='')
                        print(spaces, end='')
                        if i == 4 and is_perfect(x) == True:
                            print('  x', end='')
                        print(spaces, end='')
                        if i == 5 and is_abundant(x) == True:
                            print('   x', end='')
                    # End choice 4 once the last number's information has been displayed
                    if is_all_n2 == x:
                        print()
                        condition_2 = False
        # End program if user input is 5
        if choice == 5:
            print()
            print('Goodbye!')
            condition_1=False
            break
        
        
        

                    
                        
                    
                    
            

                             
            
            
            
            
                                 
                        
