# Luke Psyhogios, 1 February 2022, Section 001, Problem #2: Using the print function

# Ask user to enter three seperate countries
country1 = input('Please enter country #1: ')
country2 = input('Please enter country #2: ')
country3 = input('Please enter country #3: ')

# Display line-break
print()
# Display top of list
print('Here are your countries in every possible order:')
print('--------------------------------------------')
print()
# Display countries in order of country1, country2, country3 seperated by commas
print('1. ', end="")
print(country1, country2, country3, sep = ", ")
print()
"""
Display countries in order of country1, country3, country2
seperated by '***' before and after each country name
"""
print('2. ***', end="")
print(country1, country3, country2, sep = '*** ***', end="")
print('***')
print()
# Display countries in order of country2, country1, country3 seperated by ':' and no space
print('3. ', end = '')
print(country2, country1, country3, sep=':')
print()
# Display countries in order of country2, country3, country1 each on a different line
print('4. ', country2)
print(country3)
print(country1)
print()
"""
Display countries in order of country3, country2, country1 each on a different line
equidistant from the start of the line. Display '?' after country3, '!' after country2,
and '?!' after country1

"""
print('5. ', end='')
print(country3, '?', sep='')
print('   ', country2, '!', sep='')
print('   ', country1, '?!', sep='')
print()
"""
Display countries in order of coutry3, country1, country2. Diplay '--' after country3,
'-----' after country1, and '-------' after country2
"""
print('6. ', end='')
print('--', country3, sep='')
print('   ', '-----', country1, sep='')
print('   ', '-------', country2, sep='')

