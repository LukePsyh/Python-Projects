# Luke Psyhogios, May 2nd 2022, Section 001, Assignment 10, Problem #1
# Set conditional variables
valid_1 = True
valid_2 = True
valid_3 = True

# Set up dictionary
inventory = {
 'soft drink': [0.99, 10],
 'onion rings': [1.29, 5],
 'small fries': [1.49, 20]
 }

while valid_1 == True:
     # Ask user for choice
     choice = input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ')
     # If user selects l...
     if choice == 'l':
         # ...list the products
         print('Product' + '\t' + '\t' + 'Price' + '\t' + 'Quantity')
         for k in inventory:
             k = str(k)
             if ' ' in k:
                print(k + '\t' + str(inventory[k][0]) + '\t' + str(inventory[k][1]))
             else:
                print(k + '\t' + '\t' + str(inventory[k][0]) + '\t' + str(inventory[k][1]))
     # If user selects s...
     elif choice == 's':
        search_item = input('Enter a product name: ')
        search_item = search_item.lower()
        if search_item in inventory:
            # ...print item and price
            print('We sell', search_item, 'at', inventory[search_item][0])
        else:
            print("Sorry, we don't sell", search_item)
     # If user selects a...
     elif choice == 'a':
         new_product = input('Enter a product name: ')
         # Ensure no duplicate products
         if new_product in inventory:
             print('Duplicate product name')
         else:
            while valid_2 == True:
                new_product = new_product.lower()
                new_price = float(input('Enter a price: '))
                new_price = format(new_price, '.2f')
                new_price = float(new_price)
                if new_price < 0.01:
                    print('Invalid range, try again')
                else:
                    valid_2 = False
                    while valid_3 == True:
                        new_quan = int(float(input('Enter an inventory amount: ')))
                        # Ensure valid quantity is entered
                        if new_quan < 1 or new_quan > 100:
                            print('Invalid range, try again')
                        else:
                            valid_3 = False
                            # ... add product to the inventory
                            inventory.update({new_product: [new_price, new_quan]})
                            print('Product added')
     # If user selects r...
     elif choice == 'r':
         prod_remove = input('Enter a product name: ')
         #... remove the product from the inventory
         if prod_remove in inventory:
             inventory.pop(prod_remove)
             print('Product removed')
         # Ensure the product exists in the inventory
         else:
             print('Unknown product name')
     # If user selects u...
     elif choice == 'u':
         prod_update = input('Enter a product name: ')
         # Ensure product that needs updating exists
         if prod_update not in inventory:
             print('Product does not exist')
             continue
         # ... update name, price or amount
         update_choice = input('(n)ame, (p)rice or (a)mount? ')
         if update_choice == 'n':
             new_name = input('Enter a new name: ')
             new_name = new_name.lower()
             if new_name in inventory.keys():
                 print('Product name already exists') 
                 continue
             else:
                 # Update product name
                 update_price = inventory[prod_update][0]
                 update_quantity = inventory[prod_update][1]
                 inventory.pop(prod_update)
                 inventory[new_name] = update_price, update_quantity
                 print('Product renamed')
         elif update_choice == 'p':
             new_price = float(input('Enter a new price: '))
             new_price = format(new_price, '.2f')
             new_price = float(new_price)
             # Update product price 
             inventory[prod_update][0] = new_price
             print('Product price updated')
         elif update_choice == 'a':
             new_amount = int(float(input('Enter a new quantity: ')))
             new_amount = format(new_amount, '.2f')
             new_amount = int(float(new_amount))
             # Update product quantity
             inventory[prod_update][1] = new_amount
             print('Product quantity updated')
         # Ensure a valid choice is selected
         else:
             print('Invalid choice')
     # If user selects e...
     elif choice == 'e':
         # Set variables
         total = float(0)
         list = []
         high = 0
         low = 99999999999999999999999999999999999999999
         for k in inventory:
             value = inventory[k][0] * inventory[k][1]
             # Find the highest price value
             if inventory[k][0]>high:
                 high = inventory[k][0]
                 high_product = k
             # Find th lowest price value
             if inventory[k][0]<low:
                 low = inventory[k][0]
                 low_product = k
             total += value
         total = format(total, '.2f')
         # ... report the data
         print('Total cost of all items in inventory: ', total)
         print('Highest priced item: ', high, 'is', high_product)
         print('Lowest priced item: ', low, 'is', low_product)
     # If user selects q...
     elif choice == 'q':
         # ... end the program
         print('See you soon!')
         valid_1 = False
     else:
         print('Unknown command, try again')
