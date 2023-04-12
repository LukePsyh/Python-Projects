# Luke Psyhogios, April 11th 2022, Section 001, Assignment 7, Problem #2a: Cryptography

# Import functions
from PsyhogiosLuke_assignment7_part2a import add_letters
from PsyhogiosLuke_assignment7_part2a import delete_characters
from PsyhogiosLuke_assignment7_part2a import flip
from PsyhogiosLuke_assignment7_part2a import ascii_shift
from PsyhogiosLuke_assignment7_part2a import shift_left
from PsyhogiosLuke_assignment7_part2a import shift_right
import random

# Set conditional/accumulator variables
valid = True
accumulator = ''

while valid == True:
    # Ask user to input pattern
    pattern = str(input("Enter an encoding pattern, 'end' to end: "))
    if pattern == 'end':
        break
    # Ask user for string to encode/decode
    word = str(input("Enter a word to encode/decode: "))
    for character in pattern:
        # Print star for formatting
        print('*', end='', sep='')
        # (For all if and elif statements here) if character == n execute action which lines up with n (i.e. 'A' and add_letters)
        if character == 'A':
            word = add_letters(word, 1)
            print('Added 1 character:', word)
        elif character == 'X':
            word = delete_characters(word, 1)
            print('Deleted 1 character:', word)
        elif character == 'F':
            word = flip(word)
            print('Flipped:', word)
        elif character == 'U':
            word = ascii_shift(word, 1)
            print('ASCII shifted up:', word)
        elif character == 'D':
            word = ascii_shift(word, -1)
            print('ASCII shifted down:', word)
        elif character == 'L':
            word = shift_left(word)
            print('Shifted left:', word)
        elif character == 'R':
            word = shift_right(word)
            print('Shifted right:', word)
        else:
            print('Invalid character, moving onto next character in pattern')
            continue
        word = word
        

