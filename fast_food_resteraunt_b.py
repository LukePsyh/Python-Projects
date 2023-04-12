# Luke Psyhogios, April 17th 2022, Section 001, Assignment 8, Problem #2b: Fast Food Restaurant

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantities = [10, 5, 20]

# Conditional variables
valid_1 = True

# Extra variables
length = len(product_names)
iterations = 0

# While loop so user can choose when to exit
while valid_1 == True:
    action = input('(s)earch, (l)ist or (q)uit: ').lower()
    if action == 's':
        user_selection = input('Enter a product name: ').lower()
        if user_selection in product_names:
            # Find corresponding index to the product
            product_index = product_names.index(user_selection)
            # Display output
            print('We sell', user_selection, 'at', product_costs[product_index], 'per unit')
            print('We currently have', product_costs[product_index], 'in stock')
            print('\n')
        else:
            # Display output
            print("Sorry, we don't sell", user_selection)
            print('\n')
    elif action == 'q':
        # Display output
        print('See you soon!')
        valid_1 = False
    elif action == 'l':
        #Display output
        print('Product', '\t'*2, 'Price', '\t', 'Quantity')
        for i in range(length):
            # Display product data
            print(product_names[iterations], '\t', product_costs[iterations], ' ', product_quantities[iterations])
            iterations += 1
        print('\n')
    else:
        print('Invalid option, try again')
        print('\n')
        
        
        
