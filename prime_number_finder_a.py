# Luke Psyhogios, March 9th 2022, Section 001, Problem #2a: Prime Number Finder

# Set conditional variables
valid = False
valid_2 = False

# Validate user input
while valid == False:
    # Ask user for input
    n = int(input('Enter a positive number to test: '))
    if n>1:
        valid = True
    # If user inputs 1 display this output
    elif n == 1:
        print()
        print('1 is technically not a prime number.')
        valid = True
        valid_2 = True
    else:
        print('Not a positive number. Try again.')
        
for i in range(2, n):
    # If n%1 == 0 the number is not prime 
    if n%i == 0:
        print(i, 'is a divisor of', n, '... stopping')
        print()
        print(n, 'is not a prime number.')
        valid_2 = True
        break
    else:
        print(i, 'is NOT a divisor of', n, '... continuing')
# Print if n is prime        
if valid_2==False:
    print()
    print(n, 'is a prime number!')
    
    
