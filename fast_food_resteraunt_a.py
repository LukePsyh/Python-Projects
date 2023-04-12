# Luke Psyhogios, April 17th 2022, Section 001, Assignment 7, Problem #2a: Fast Food Restaurant

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]

# Conditional variables
valid_1 = True

# While loop so user can choose when to exit
while valid_1 == True:
    action = input('(s)earch for product or (q)uit: ').lower()
    if action == 's':
        user_selection = input('Enter a product name: ').lower()
        if user_selection in product_names:
            # Find corresponding index to the product
            product_index = product_names.index(user_selection)
            # Display output
            print('We sell', user_selection, 'at', product_costs[product_index], 'per unit')
            print('\n')
        else:
            # Display output
            print("Sorry, we don't sell", user_selection)
            print('\n')
    elif action == 'q':
        # Display output
        print('See you soon!')
        valid_1 = False
    else:
        print('Invalid option, try again')
        print('\n')
    
        
        
        
        
