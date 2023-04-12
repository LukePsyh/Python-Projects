# Luke Psyhogios, February 9th 2022, Section 001, Problem #1: Math with Place Values

# Ask user for numbers
first_number = int(input('Enter a number between 0 and 999: '))
second_number = int(input('Enter another number between 0 and 999: '))


# Compute ones place of both numbers
first_number_ones = first_number % 10
second_number_ones = second_number % 10


# Compute sum of ones
sum_of_ones = first_number_ones+second_number_ones

# Reassign variables
first_number = first_number//10
second_number = second_number//10

# Compute tens place of both numbers
first_number_tens = first_number % 10
second_number_tens = second_number % 10

# Compute product of tens
product_of_tens = first_number_tens*second_number_tens

# Compute hundreds place
first_number_hundreds = first_number//10
second_number_hundreds = second_number//10

# Compute difference of hundreds
difference_of_hundreds = first_number_hundreds-second_number_hundreds

# Diplay output
print("Sum of ones     =", first_number_ones, '+',second_number_ones, '=', sum_of_ones)
print("Product of tens     =", first_number_tens, '*', second_number_tens, '=', product_of_tens)
print("Difference of hundreds =", first_number_hundreds, '-', second_number_hundreds, '=', difference_of_hundreds)
