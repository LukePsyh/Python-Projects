# Luke Psyhogios, April 17th 2022, Section 001, Assignment 7, Problem #2c: Fast Food Restaurant

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantities = [10, 5, 20]
print(type(product_costs))

# Conditional variables
valid_1 = True
valid_2 = True
valid_3 = True

# Extra variables
length = len(product_names)
iterations = 0

# While loop so user can choose when to exit
while valid_1 == True:
    # Conditional variables
    valid_2 = True
    valid_3 = True
    valid_4 = True
    action = input('(s)earch, (l)ist, (a)dd or (q)uit: ').lower()
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
    elif action == 'a':
        while valid_2 == True:
            # Get data from user
            user_entry = input('Enter a new product name: ')
            if user_entry in product_names:
                # Incase the product is already on the menu
                print('Sorry, we already sell that product. Try again.')
                continue
            else:
                valid_2 = False
            while valid_3 == True:
                # Get the new product cost
                new_cost = float(input('Enter a product cost: '))
                if new_cost<0:
                    # Ensure the product price is above 0
                    print('Invalid cost. Try again.')
                    continue
                else:
                    valid_3 = False
                while valid_4 == True:
                    # Get new quantity of the product
                    new_quantity = int(input('How many of these products do we have? '))
                    if new_quantity<1:
                        print('Invalid quantity. Try again.')
                        continue
                    else:
                        # Add data to lists
                        product_names = product_names.append(user_entry)
                        product_costs = product_costs.append(new_cost)
                        product_quantities = product_quantities.append(new_quantity)
                        print('Product added!')
                        print('\n')
                        valid_4 = False
    else:
        print('Invalid option, try again')
        print('\n')
        
        
        
