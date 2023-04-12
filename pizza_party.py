# Luke Psyhogios, March 9th 2022, Section 001, Problem #0: Pizza Party

# Ask user for their party budget
budget = float(input('Enter budget for your party: '))

# Ask user for the cost per pizza slice
price_per_slice = float(input('Cost per slice of pizza: '))

# Ask user for the cost of the whole pie
price_per_pie = float(input('Cost per whole pizza pie (8 slices): '))

# Ask user for number of attendees
guests = int(input('How many people will be attending your party? '))

# Set slices equal to zero
total_slices = 0

for i in range(1, guests+1):
    # Set conditional variable
    valid = False
    # Validate data entry
    while valid == False:
        slices = int(input('Enter a number of slices for person #'+str(i)+': '))
        if slices > 0:
            valid = True
            total_slices += slices
        else:
            print('Not a valid entry, try again!')
            print()

# Compute variables for display
pies = total_slices//8
slices_leftover = total_slices%8
total_cost = pies*price_per_pie + slices_leftover*price_per_slice
remaining = budget - total_cost
formatted_total_cost = format(total_cost, '.2f')
formatted_remaining = format(remaining, '.2f')

# If user goes over budget convert negative remaining balance into a positive
# number for display
over_budget = abs(remaining)
formatted_over_budget = format(over_budget, '.2f')

# If the total cost of the party is within the budget
if budget > total_cost:
    print('You should purchase', pies, 'pies and', slices_leftover, 'slices')
    print("Your total cost will be:", formatted_total_cost)
    print('You will stil have', formatted_remaining, 'left after your order')

# If the total cost of the party is equal to the budget
elif budget == total_cost:
    print('You should purchase', pies, 'pies and', slices_leftover, 'slices')
    print('Your total cost will be:', formatted_total_cost)
    print('You will have no money left after your order.')

# If the total cost of the party is greater than the budget
else:
    print('Your order cannot be completed.')
    print('You would need to purchase', pies, 'pies and', slices_leftover, 'slices')
    print('This would put you over your budget by', formatted_over_budget)
    


             
