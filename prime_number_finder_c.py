# Luke Psyhogios, March 9th 2022, Section 001, Problem #2c: Custom Number Range

# Set conditional variables
valid_1 = False
valid_2 = False

# Validate start and end numbers
while valid_1 == False or valid_2 == False:
    # Ask user for input
    start = int(input('Start number: '))
    end = int(input('End number: '))
    # Validate that both numbers are positive
    if start >= 1 and end >= 1:
        valid_1 = True
    else:
        print('Start and end must be positive')
        continue
    # Validate that end number is larger than start number
    if start<end:
        valid_2 = True
    else:
        print('End number must be greater than start number')

print()

for n in range(start, end):
    for i in range(2,n):
        # If n%i is equal to zero between 2 and n then n is not a prime number
        if n%i == 0:
            break
    else:
        # Display output
        if n != 1:
            print(n)
    if n == 1:
             print(n, 'is technically not a prime number')
             
