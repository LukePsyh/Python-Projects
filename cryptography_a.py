# Luke Psyhogios, April 11th 2022, Section 001, Assignment 7, Problem #2a: Cryptography

# function: ascii_shift
# input: a word to shift (String) and an amount to shift by (integer)
# processing: shifts each character in the supplied word to another position
# in the ASCII table. the new position is dictated by the supplied
# integer. for example, if word = "apple" and num=1the newly generated word would be:
# bqqmf
# because we added +1 to each character.
# if we were to call the function with
# word = "bqqmf" and num=-1 the newly generated word would be:
# apple
# because we added -1 to each character, which shifted
# each character down by one position on the ASCII table.
# in the event that an empty string is supplied no shift
# will occur and an empty string should be returned
# output: returns the newly generated word
def ascii_shift(word, n):
    # Set initial variables
    string = ''
    i = 0
    for character in word:
        # Set value
        value = int(ord(word[i]))
        # Change value for for loop to work
        i += 1
        value += n
        value = chr(value)
        value = str(value)
        # Add new character to string
        string = string + value
        # End loop if completed
        if len(word) == len(string):
            return string

# function: shift_right
# input: a word to shift (String)
# processing: shifts all characters in the string to the right. the last char
# acter in the string will be shifted to the beginning of
# the string. for example:
# apple -> eappl
# in the event that an empty string is supplied
# no shift will occur and an empty string should be returned
# output: returns the newly generated word
def shift_right(word):
    # Start from the right end of the word
    new_word = str(word[-1])
    # Shift the word to the right
    for i in range(0, len(word)-1):
        new_letter = word[i]
        new_word += new_letter
    # Return new word
    return new_word


# function: shift_left
# input: a word to shift (String)
# processing: shifts all characters in the string to the left.
# the first character in the string
# will be shifted to the end of the string. for example:
# apple -> pplea
# in the event that an empty string is supplied
# no shift will occur and an empty string should be returned
# output: returns the newly generated word
def shift_left(word):
    # Start from the second character
    new_word = str(word[1])
    # Shift the word to the left
    for i in range(2, len(word)):
        new_letter = word[i]
        new_word += new_letter
        if len(word)-1 == i:
            new_word += word[0]
    # Return shifted word
    return new_word


# function: flip
# input: a word to flip (String)
# processing: flips the first half of the string with the second half of the
# string. if the string has an even number of characters
# this function will work as follows:
# ABCD -> CDAB
# if the string has an odd number of characters this function
# will work as follows:
# ABCDE -> DECAB
# in the event that an empty string is supplied no flip
# will occur and an empty string should be returned
# output: returns the newly generated word
def flip(word):
    # Set variables
    length = len(word)
    new_string = ''
    # If the length of the string is even...
    if length%2 == 0:
        # Set variables
        n = int(length/2)
        n_two = int(length)
        # Set first half of string
        for i in word[n:n_two]:
            new_string +=i
        # Set second half of string
        for i in word[0:n]:
            new_string +=i
        return new_string
    # ...else
    else:
        # Set variables
        n_one = int((length)/2)+1
        n_two = int(length)
        n_three = int((length-1)/2)
        n_four = int((length-2)/2)
        # Set first half of string
        for i in word[n_one:n_two+1]:
            new_string +=i
        # Add middle letter
        new_string += word[n_three]
        # Set second half of string
        for i in word[0:n_four+1]:
            new_string +=i
        return new_string

# function: add_letters
# input: a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter
# in the supplied word. for example, if word="cat" and num=1
# we could generate any of the following:
# cZaQtR
# cwaRts
# cEaett
# if word="cat" and num=2 we could generate any of the following:
# cRtaHFtui
# cnnaNYtjn
# czAaAitym
# output: returns the newly generated word

import random

def add_letters(word, n):
    word = str(word)
    n = int(n)
    # Set variables
    l = []
    string = ''
    # Create list with every letter in the alphabet; both uppercase and lowercase
    for i in range(65,91):
        x = chr(i)
        l += x
    for i in range(97,123):
        x = chr(i)
        l += x
    for character in word:
        random_chrs = ''
        for i in range(n):
            # Randomly select two items from the list
            new_chr_loco = random.randint(0,51)
            new_chr = str(l[new_chr_loco])
            # Attach the random characrers to the character from the word
            random_chrs += new_chr
        string += character + random_chrs
    return string
# function: delete_characters
# input: a word to analyze (String) and the number of characters
# to remove (integer)
# processing: the function starts at the first position in the supplied word
# and keeps it. it then removes "num" characters from the word.
# the process is repeated again if the word contains additional
# characters - the next character is kept and "num" more
# characters are removed. For example, if word="cZaYtU" and
# num=1 the function will generate the following:
# cat (keeping character 0, removing character 1, keeping
# character 2, removing character 3, keeping character 4,
# removing character 5)
# output: returns the newly unscrambled word
def delete_characters(word, n):
    word = str(word)
    n = int(n)
    # Set variables
    length = len(word)
    s = ''
    # Add correct characters to the right string using string slicing
    for character in word[0:length:n+1]:
        s += character
    return s
        
        
        





           
           
            
        
