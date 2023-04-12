# Luke Psyhogios, March 9th 2022, Section 001, Problem #3: Multiplication Table

# Set conditional variable for data validation of low number
valid_1 = False
low_n = 0

# while loop for data validation of low number
while valid_1 == False:
    # Get low number from user
    low_n = int(input('Lowest number: '))
    if low_n<0:
            print('Lowest number must be 0 or greater')
    # Break loop if the integer entered is positive
    else:
            valid_1 = True

# Set conditional variable for data validation of high number
valid_2 = False

# While loop for data validation of high number
while valid_2 == False:
    # Get high number from user
    high_n = int(input('Highest number: '))
    if high_n < low_n:
        print('Highest number must be larger than lowest number!')
    # Break loop if high_n > low_n
    else:
        valid_2 = True

# Set up formatting variables
number = len(str(high_n**2))
form = '>' + str(number) + 'd'
form_s = '>' + str(number) + 's'

# Display top of output with for loop
print()
print(' ' + format('+', form_s), end='')
for i in range(low_n, high_n+1):
    # Display formatted top row
    custom_str = ("  " + format(i, form))
    print(custom_str, end = '')
    
print()
# Display dashes
print("-"*(number + 1), end = "")
for i in range(low_n, high_n + 1):
    if i == high_n:
        print("-"*(number + 2))
    else:
        print("-"*(number + 2), end = "")


# Display multiplication table
for x in range(low_n, high_n+1):
    # Display leftmost column
    print(format(x, form), '| ', end='')
    # Display multiplication results
    for y in range(low_n, high_n+1):
        if y<high_n:
            print(format(x*y, form), ' ', end='')
        if y==high_n:
            print(format(x*y, form))
        


   



                 


                
 
