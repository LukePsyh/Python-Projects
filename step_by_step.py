# Luke Psyhogios, March 9th 2022, Section 001, Problem #1: Step by Step
 
# Set conditional variable
valid = False

# Validate that the user entered a valid number
while valid == False:
    n = int(input('Pick a number to go up to: '))
    if n > 0:
        valid = True
    else:
        print('Invalid, try again.')
# Set initial variables
line = 0
old_line = ''
final_line = ''
for i in range(1, n+1):
    line = str(i)
    for x in [1]:
        # Add old line to new digit
        total_line = old_line + ' ' + line
        old_line = total_line
        # Display numbers
        print(total_line)
        
        
            
