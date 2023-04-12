# Luke Psyhogios, February 16th 2022, Section 001, Problem #0: Two Rectangles (Warm-Up)

# Ask user to enter the dimensions for two seperate rectangles
width_one = int(input('Enter the width for Rectangle #1: '))
length_one = int(input('Enter the length for Rectangle #2: '))
width_two = int(input('Enter the width for Rectangle #2: '))
length_two = int(input('Enrer the length for Rectangle #2: '))

# Compute areas
area_one = width_one*length_one
area_two = width_two*length_two

# Display output
print('Rectangle #1 has an area of', area_one)
print('Rectangle #2 has an area of', area_two)

# Use if statements to determine which rectangle is larger
if area_one>area_two:
    print('Rectangle #1 is larger than Rectangle #2')
if area_one==area_two:
    print('Rectangle #1 and Rectangle #2 are the same size')
if area_two>area_one:
    print('Rectangle #2 is larger than Rectangle #1')

# Use if statements to determine if either rectangle is a square
if width_one==length_one:
    print('Rectangle #1 is a square')
if width_two==length_two:
    print('Rectangle #2 is a square')
