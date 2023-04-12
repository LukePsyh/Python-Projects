# Luke Psyhogios, February 9th 2022, Section 001, Problem #2: Distance Calculator

# Ask the user for the components of each object
x_one = int(input("What is object #1's x component? "))
y_one = int(input("What is object #1's y component? "))
x_two = int(input("What is object #2's x component? "))
y_two = int(input("What is object #2's y component? "))

# Compute x and y distances
x_distance = abs(x_one-x_two)
y_distance = abs(y_one-y_two)

# Compute distance
distance = ((x_two-x_one)**2+(y_two-y_one)**2)**0.5

# Format distance
distance = format(distance, '.2f')

# Display output
print('Distance calculator')
print('Object #1 x:', x_one)
print('Object #1 y:', y_one)
print('Object #2 x:', x_two)
print('Object #2 y:', y_two)
print()
print('X distance:', x_distance)
print('Y distance:', y_distance)
print('Straight line distance:', distance)
