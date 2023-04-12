# Luke Psyhogios, April 17th 2022, Section 001, Assignment 7, Problem #2d: Fast Food Restaurant

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_quantities = [10, 5, 20]

# Conditional variables
valid_1 = True
valid_2 = True
valid_3 = True


# While loop so user can choose when to exit
while valid_1 == True:
    # Conditional variables
    valid_2 = True
    valid_3 = True
    valid_4 = True
    valid_5 = True
    valid_6 = True
    valid_7 = True
    # Extra variables
    length = len(product_names)
    iterations = 0
    action = input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ').lower()
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
    elif action == 'r':
        user_remove = input('Enter a product name: ').lower()
        # If the product exits, remove it and all it's data from the lists
        if user_remove in product_names:
            name_index = product_names.index(user_remove)
            cost = product_costs[name_index]
            quantity = product_quantities[name_index]
            product_names.remove(user_remove)
            product_costs.remove(cost)
            product_quantities.remove(quantity)
            print('Product removed')
            print('\n')
        else:
            print("Product doesn't exist. Can't remove.")
    elif action == 'u':
        product_update = input('Enter a product name: ')
        new_index = product_names.index(product_update)
        if product_update in product_names:
            print('What would you like to update?')
            update_action = input('(n)ame, (c)ost or (q)uantity: ')
            if update_action == 'n':
                while valid_5 == True:
                    new_product = input('Enter a new name: ')
                    if new_product in product_names:
                        print('Duplicate name!')
                        continue
                    else:
                        product_names[new_index] = new_product
                        print('Product name has been updated')
                        print('\n')
                        valid_5 = False
            elif update_action == 'c':
                while valid_6 == True:
                    new_price = float(input('Enter a new cost: '))
                    if new_price <= 0:
                        print('Invalid cost!')
                        continue
                    else:
                        product_costs[new_index] = new_price
                        print('Product cost has been updated')
                        print('\n')
                        valid_6 = False
            elif update_action == 'q':
                while valid_7 == True:
                    new_quantity = int(input('Enter a new quantity: '))
                    if new_quantity <= 1:
                        print('Invalid quantity!')
                        continue
                    else:
                        product_quantities[new_index] = new_quantity
                        print('Product quantity has been updated')
                        print('\n')
                        valid_7 = False
            else:
                print('Invalid option')
        else:
            print("Product doesn't exist. Can't update.")
    elif action == 'e':
        total_cost_list = []
        high_cost = max(product_costs)
        low_cost = min(product_costs)
        high_cost_index = product_costs.index(high_cost)
        low_cost_index = product_costs.index(low_cost)
        high_cost = str(max(product_costs))
        low_cost = str(min(product_costs))
        for i in range(0, len(product_costs)):
            total_cost_list.append(product_costs[i] * product_quantities[i])
            total_cost = sum(total_cost_list)      
        total_cost = format(total_cost, '.2f')
        total_cost = str(total_cost)
        print('Most expensive product:' + '      ' + high_cost + '(' + product_names[high_cost_index] + ' )')
        print('Least expensive product:' + '     ' + low_cost + '(' + product_names[low_cost_index]+ ' )')
        print('Total value of all products: ' + total_cost)
        print('\n')
    else:
        print('Invalid option, try again')
        print('\n')





        
        
