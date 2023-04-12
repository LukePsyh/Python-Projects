# Luke Psyhogios, February 28th 2022, Section 001, Problem #3: Math Quiz

# Assign conditional variable
question_number = 1

# Set initial test answers correct to zero
score = 0

# Import randint from random
from random import randint


while question_number <= 5:
    # set variables in Questions to random integers
    x = randint(1,10)
    y = randint(1,10)
    # randomly assign the + - or * function to each
    operator_int = randint(1,3)
    if operator_int == 1:
        operator = '+'
    if operator_int == 2:
        operator = '-'
    if operator_int == 3:
        operator = '*'
    if question_number == 1:
        # Print question 1
        print('Question ', question_number, '. ', x, ' ' , operator, ' ', y, sep='')
        # Set proper answer based on random operation
        if operator == '+':
            answer = x+y
        if operator == '-':
            answer = x-y
        if operator == '*':
            answer = x*y
        # Ask user to input their first answer
        student_ans = float(input('What is the answer? '))
        if student_ans == answer:
            print('Correct!')
            # Add a point to their score for every correct answer
            score += 1
            # End of question so add one to question_number in order for next question
            question_number += 1
            continue
        else:
            print('Incorrect!')
            question_number += 1
            continue
    if question_number == 2:
        # Print question 2
        print('Question ', question_number, '. ', x, ' ' , operator, ' ', y, sep='')
        if operator == '+':
            answer = x+y
        if operator == '-':
            answer = x-y
        if operator == '*':
            answer = x*y
        # Ask user to input their second answer
        student_ans = float(input('What is the answer? '))
        if student_ans == answer:
            print('Correct!')
            score += 1
            question_number += 1
            continue
        else:
            print('Incorrect!')
            question_number += 1
            continue
    if question_number == 3:
        # Print question 3
        print('Question ', question_number, '. ', x, ' ' , operator, ' ', y, sep='')
        if operator == '+':
            answer = x+y
        if operator == '-':
            answer = x-y
        if operator == '*':
            answer = x*y
        # Ask user to input their third answer
        student_ans = float(input('What is the answer? '))
        if student_ans == answer:
            print('Correct!')
            score += 1
            question_number += 1
            continue
        else:
            print('Incorrect!')
            question_number += 1
            continue
    if question_number == 4:
        # Print question 4
        print('Question ', question_number, '. ', x, ' ' , operator, ' ', y, sep='')
        if operator == '+':
            answer = x+y
        if operator == '-':
            answer = x-y
        if operator == '*':
            answer = x*y
        # Ask user to input their fourth answer
        student_ans = float(input('What is the answer? '))
        if student_ans == answer:
            print('Correct!')
            score += 1
            question_number += 1
            continue
        else:
            print('Incorrect!')
            question_number += 1
            continue
    if question_number == 5:
        # Print question 5
        print('Question ', question_number, '. ', x, ' ' , operator, ' ', y, sep='')
        if operator == '+':
            answer = x+y
        if operator == '-':
            answer = x-y
        if operator == '*':
            answer = x*y
        # Ask user to input their fifth answer
        student_ans = float(input('What is the answer? '))
        if student_ans == answer:
            print('Correct!')
            score += 1
            question_number += 1
        else:
            print('Incorrect!')
            question_number += 1
    # Assign test scores to their proper grades
    grade = 'none'
    if score == 5:
        grade = 'A'
    if score == 4:
        grade = 'B'
    if score == 3:
        grade = 'C'
    if score == 2:
        grade = 'D'
    if score <2:
        grade = 'F'
    # Print results
    print('You received', score, 'out of a possible 5 points.')
    print('You scored a ', grade, '.', sep='')



















          
