# Luke Psyhogios, February 28th 2022, Section 001, Problem #1: Roll the Dice

# Create condition1 to check if the user inputs a valid number of sides for the dice
condition1 = False

# Confirm that user inputs a valid number of sides
while condition1 == False:
    sides = int(input('How many sides on your dice (4, 6, 8)? '))
    if sides == 4 or 6 or 8:
        print()
        print('Thanks, here we go!')
        print()
        condition1 = True
    else:
        print('Invalid size, try again.')
        
# Import randint
from random import randint

# Assign conditional variable to end loop after snake eyes are rolled
condition2 = False

# Assign all numbers that the program needs to keep count within the while loop to zero
rolls = 0
doubles = 0
odds = 0
evens = 0
high = 0
high_and_low = 0
size_is_sum = 0
die_one_count = 0
die_two_count = 0

# Run while loop to simulate dice roll
while condition2 == False:
    # randint must be assigned to die_1 and die_2 within the loop to give new numbers on every roll
    die_1 = randint(1,sides)
    die_2 = randint(1,sides)
    print('die #1 is *', die_1, '* and die #2 is *', die_2, '* ', sep='', end='')
    # Counts number of rolls until snake eyes
    rolls += 1
    # Display and keep track of doubles, two high values, two evens etc.
    if die_1 == die_2:
        print('Doubles! ', end='')
        doubles += 1
    if die_1 == (1 or 3 or 5 or 7) and die_2 == (1 or 3 or 5 or 7):
        print('Odds! ', end='')
        odds += 1
    if die_1 == (2 or 4 or 6 or 8) and die_2 == (2 or 4 or 6 or 8):
        print('Evens! ', end='')
        evens += 1
    if die_1 == sides and die_2 == sides:
        print('High Value! ', end='')
        high +=1
    if die_1 == 1 and die_2 == sides:
        print('High / Low! ', end='')
        high_and_low +=1
    elif die_2 == 1 and die_1 == sides:
        print('High / Low! ', end='')
        high_and_low += 1
    if die_1+die_2 == sides:
        print('Sum value is size value! ', end='')
        size_is_sum += 1
    # Once Snake Eyes are rolled display all results and end the loop
    if (die_1+die_2) == 2:
        print('Snake Eyes! ')
        print()
        print('You finally got snake eyes on roll #', rolls)
        print('Along the way you rolled DOUBLES ', doubles, ' times. (', int((doubles/rolls)*100), '% of all rolls were doubles)', sep='')
        print('Along the way you rolled TWO HIGH VALUES ', high, ' times. (', int((high/rolls)*100), '% of all rolls were two high values)', sep='')
        print('Along the way you rolled TWO EVENS ', evens, ' times. (', int((evens/rolls)*100), '% of all rolls were two evens)', sep='')
        print('Along the way you rolled TWO ODDS ', odds, ' times. (', int((odds/rolls)*100), '% of all rolls were two odds)', sep='')
        print('Along the way you rolled HIGH / LOW ', high_and_low, ' times. (', int((high_and_low/rolls)*100), '% of all rolls were high/low)', sep='')
        print('Along the way you rolled A SUM VALUE ', size_is_sum, ' times. (', int((size_is_sum/rolls)*100), '% of all rolls were a sum value)', sep='')
        condition2 = True
    die_one_count += die_1
    die_two_count += die_2
    if (die_1+die_2) == 2:
        print('Average roll for die #1:', format(float(die_one_count/rolls), '.2f'))
        print('Average roll for die #2:', format(float(die_two_count/rolls), '.2f'))
    print()
    
        
