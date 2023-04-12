# Luke Psyhogios, March 28th 2022, Section 001, Problem #1a: Number Analyzer (PROGRAM AFTER FUNCTION DEFINITIONS)

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
# Set conditional variables for data validation
condition_1 = True
condition_2 = True

# Validate that the user enters a positive number 
while condition_1 == True:
    n1 = int(input('Enter a starting number: '))
    if n1<0:
        print('Invalid, try again')
    else:
        condition_1 = False

# Validate that the second number inputted is greater than the first    
while condition_2 == True:
    n2 = int(input('Enter ending a number: '))
    if n1>n2:
        print('Invalid, try again')
    else:
        condition_2 = False

for x in range(n1, n2+1):
    # if one of the functions evaluates to true, add that quality to an empty string
    base = ''
    if is_even(x) == True:
        base = base + 'even '
    if is_odd(x) == True:
        base = base + 'odd '
    if is_prime(x) == True:
        base = base + 'prime '
    if is_perfect(x) == True:
        base = base + 'perfect '
    if is_abundant(x) == True:
        base = base + 'abundant '
    # add the qualities of the number (saved in the variable base) to the beggining of the display
    print(x, 'is ... ' + base)
        
    





























        
        
    
        
        
        
