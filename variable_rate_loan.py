# Luke Psyhogios, February 9th 2022, Section 001, Problem #3: Variable Rate Loan

# Import randint from random package
from random import randint

# Display top of program
print('This program will project how much a variable interest-rate loan will grow over a 3-month period.')
print()

# Ask user for intial borrow amount and interest rate
starting_balance = float(input('To begin, enter how much money you would like to initially borrow (i.e. 20000): '))
lower_rate = int(input('Next, enter a lower bound for the monthly interest rate. For example, enter 5 for 5%: '))
upper_rate = int(input('Finally, enter an upper bound for the monthly interest rate. For example, enter 10 for 10%: '))
print()
print()

# Get random interest rate
interest_rate1 = randint(lower_rate, upper_rate)
interest_rate2 = randint(lower_rate, upper_rate)
interest_rate3 = randint(lower_rate, upper_rate)

# Convert interest rate to a decimal
interest_rate1 = float(interest_rate1)/100
interest_rate2 = float(interest_rate2)/100
interest_rate3 = float(interest_rate3)/100

# Calculate ending balances
ending_balance1 = (starting_balance*interest_rate1)+starting_balance
ending_balance2 = (ending_balance1*interest_rate2)+ending_balance1
ending_balance3 = (ending_balance2*interest_rate3)+ending_balance2

# Convert interest rates back into integers
interest_rate1 = int(interest_rate1*100)
interest_rate2 = int(interest_rate2*100)
interest_rate3 = int(interest_rate3*100)



# Format balances
formatted_start = format(starting_balance, ',.2f')
formatted_ending_1 = format(ending_balance1, ',.2f')
formatted_ending_2 = format(ending_balance2, ',.2f')
formatted_ending_3 = format(ending_balance3, ',.2f')

# Format characters for output
formatted_money_sign_1 = format('$', '>8s')

formatted_money_sign_2 = format('$', '>14s')
    
interest_rate1 = str(interest_rate1)

formatted_interest_rate1= format(interest_rate1, '>11s')

interest_rate2 = str(interest_rate2)

formatted_interest_rate2= format(interest_rate2, '>11s')

interest_rate3 = str(interest_rate3)

formatted_interest_rate3= format(interest_rate3, '>11s')


# Display output
print(' ------- Calculating ------- ')
print()
print('Month   Starting Balance   Interest Rate   Ending Balance')
print('1', formatted_money_sign_1, formatted_start, formatted_interest_rate1, '%', formatted_money_sign_2, formatted_ending_1, sep='')
print('2', formatted_money_sign_1, formatted_ending_1, formatted_interest_rate2, '%', formatted_money_sign_2, formatted_ending_2, sep='')
print('3', formatted_money_sign_1, formatted_ending_2, formatted_interest_rate3, '%', formatted_money_sign_2, formatted_ending_3, sep='')
       
       





