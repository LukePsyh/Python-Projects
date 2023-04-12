# Luke Psyhogios, March 9th 2022, Section 001, Problem #2b: Find all Prime Numbers between 1 and 1000

# Set range to run between 1 and 1000
for n in range(1, 1001):
    for i in range(2,n):
        # If n%i is equal to zero between 2 and n then n is not a prime number
        if n%i == 0:
            break
    else:
        # Display output
        if n != 1:
            print(n, 'is a prime number!')
    if n == 1:
             print(n, 'is technically not a prime number')
             


