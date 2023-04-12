# Luke Psyhogios, May 2nd 2022, Section 001, Assignment 11, Problem #1: Gumball Machine
# Get randint function
from random import randint

# Set up class
class Gumball_Machine:
    def __init__(self, c):
        # Set up empty list for colors
        self.colors = []
        # Populate list with random colors
        for i in range(0, c):
            x = randint(1,3)
            if x == 1:
                self.colors.append('red')
            if x == 2:
                self.colors.append('green')
            if x == 3:
                self.colors.append('blue')
        self.capacity = c 
        self.money = 0
        # Announce creation
        print('Gumball machine created with', c, 'random gumballs')
    def report(self):
        # Display report
        print('Gumball Machine Report:')
        print('* Gumballs in machine:', self.capacity)
        # Format money
        form_money = format(self.money, '.2f')
        print('* Money in machine: ', form_money)
    def dispense(self, v):
        # Only accept quarters
        if v == 0.25:
            try:
                ball = self.colors[-1]
                print('Accepting 0.25; Dispensing a', ball, 'gumball')
                self.money += 0.25
                self.colors.pop(-1)
                self.capacity -= 1
            # If there are no more gumballs
            except IndexError:
                print('Machine is empty, no gumball will be dispensed')
        else:
            print('Invalid coin, no gumball will be dispensed')
    def count_gumballs_by_type(self, type_ball):
        type_ball = type_ball.lower()
        if type_ball == 'red' or type_ball == 'blue' or type_ball == 'green':
            number = self.colors.count(type_ball)
            print('There are', number, 'gumballs of type', type_ball, 'in the machine')
        else:
            print('Not a gumball color')