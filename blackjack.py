# Luke Psyhogios, February 28th 2022, Section 001, Problem #2: 21

# Print top of program
print("Let's play 21...")

# Set conditional variable
winner = False

# Import randint
from random import randint

# Set up card value and card total variables for dealer and user
card_value_user = 0
card_value_dealer = 0
user_card_total = 2
dealer_card_total = 2

# Use randint to randomly generate the cards for the user and dealer
dealer_card_one = str(randint(1,11))
dealer_card_two = str(randint(1,11))
dealer_card_three = str(randint(1,11))
user_card_one = str(randint(1,11))
user_card_two = str(randint(1,11))
user_card_three = str(randint(1,11))
user_card_four = str(randint(1,11))
user_card_five = str(randint(1,11))
user_card_six = str(randint(1,11))
user_card_seven = str(randint(1,11))
user_card_eight = str(randint(1,11))
user_card_nine = str(randint(1,11))
user_card_ten = str(randint(1,11))
user_card_eleven = str(randint(1,11))

# Format the cards for display
user_cards = user_card_one + ' ' + user_card_two
dealer_cards = dealer_card_one + ' ' + dealer_card_two



# Dispay vales of one dealer card and both user cards
print("Here are the dealer's cards:", dealer_card_one, 'X')
print('Turn: Player')
print('Here are your cards:', user_cards)
# Convert card values into integers to add the values
int_user_card_one = int(user_card_one)
int_user_card_two = int(user_card_two)
card_value_user = int_user_card_one + int_user_card_two


user_input = 'hit'
user_input = user_input.lower()
while user_input == 'hit':
    # If the card values of the user equals 21 the game should end
    if card_value_user == 21:
        print('The Player has 21!')
        print('The Player wins!')
        user_input = 'stay'
        winner = True
        break
    # If the card values of the user exceeds 21 the game should end
    if card_value_user>21:
        print('The Player goes bust!')
        print('The Dealer wins!')
        user_input = 'stay'
        winner = True
        break
    # Ask user if they would like to hit or stay
    user_input = input('What would you like to do? (Hit/Stay) ')
    user_input = user_input.lower()
    if user_input == 'hit' and user_card_total == 2:
        # If user opts to hit add the next card to their hand
        new_cards = user_cards + ' ' + user_card_three
        print('Here are your cards:', new_cards)
        int_user_card_three = int(user_card_three)
        # Keep track of user card value
        card_value_user += int_user_card_three
        # Keep track of the number of cards the user has
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 3:
        new_cards = new_cards + ' ' + user_card_four
        print('Here are your cards:', new_cards)
        int_user_card_four = int(user_card_four)
        card_value_user += int_user_card_four
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 4:
        new_cards = new_cards + ' ' + user_card_five
        print('Here are your cards:', new_cards)
        int_user_card_five = int(user_card_five)
        card_value_user += int_user_card_five
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 5:
        new_cards = new_cards + ' ' + user_card_six
        print('Here are your cards:', new_cards)
        int_user_card_six = int(user_card_six)
        card_value_user += int_user_card_six
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 6:
        new_cards = new_cards + ' ' + user_card_seven
        print('Here are your cards:', new_cards)
        int_user_card_seven = int(user_card_seven)
        card_value_user += int_user_card_seven
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 7:
        new_cards = new_cards + ' ' + user_card_eight
        print('Here are your cards:', new_cards)
        int_user_card_eight = int(user_card_eight)
        card_value_user += int_user_card_eight
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 8:
        new_cards = new_cards + ' ' + user_card_nine
        print('Here are your cards:', new_cards)
        int_user_card_nine = int(user_card_nine)
        card_value_user += int_user_card_nine
        user_card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 9:
        new_cards = new_cards + ' ' + user_card_ten
        print('Here are your cards:', new_cards)
        int_user_card_ten = int(user_card_ten)
        card_value_user += int_user_card_ten
        card_total += 1
        continue
    if user_input == 'hit' and user_card_total == 10:
        new_cards = new_cards + ' ' + user_card_eleven
        print('Here are your cards:', new_cards)
        int_user_card_eleven = int(user_card_eleven)
        card_value_user += int_user_card_eleven
        user_card_total += 1
        continue
    # If user opts to stay the program should move on from the loop
    if user_input == 'stay':
        break

# Compute the card value of the dealer
int_dealer_card_one = int(dealer_card_one)
int_dealer_card_two = int(dealer_card_two)
card_value_dealer = int_dealer_card_one + int_dealer_card_two

# If the dealer's card value equals 21 the game should end
while card_value_dealer == 21 and winner == False:
    if card_value_dealer == 21:
        print("Here are the dealer's cards:", dealer_card_one, dealer_card_two)
        print('The Dealer has 21!')
        print('The Dealer wins!')
        winner = True
        break
# If the dealer's initial two cards exceed 16, the following loop will be executed
while card_value_dealer > 16 and winner == False:
    print("Here are your cards:", dealer_card_one, dealer_card_two)
    print('The Player has ', card_value_user, ' and the dealer has ', card_value_dealer, '.', sep='')
    # Dealer wins by a higher score
    if card_value_dealer > card_value_user:
        print('The Dealer wins!')
        winner = True
        break
    # User wins by a higher score
    if card_value_user > card_value_dealer:
        print('The Player wins!')
        winner = True
        break
    # Tie
    if card_value_dealer == card_value_user:
        print("It's a tie!")
        winner = True
        break

# If the dealer's initial two cards do not exceed 16, the following loop will be executed
while card_value_dealer <= 16 and winner == False:
    print('Turn: Dealer')
    print("Here are the dealer's cards:", dealer_card_one, dealer_card_two)
    print('Your cards total to 16 or less. You must take another card.')
    print("Here are your cards:", dealer_card_one, dealer_card_two, dealer_card_three)
    # Convert third card into integer to perform calculations
    int_dealer_card_three = int(dealer_card_three)
    card_value_dealer = card_value_dealer + int_dealer_card_three
    # Ensure that with a third card the dealer's card value does not equal 21
    if card_value_dealer == 21:
        print('The Dealer has 21!')
        print('The Dealer wins!')
        winner = True
        break
    # Ensure that with a third card the dealer's card value has not exceeded 21
    if card_value_dealer > 21:
        print('The Dealer goes bust!')
        print('The Player wins!')
        winner = True
        break
    print('The Player has ', card_value_user, ' and the dealer has ', card_value_dealer, '.', sep='')
    # Dealer wins by a higher score
    if card_value_dealer > card_value_user:
        print('The Dealer wins!')
        winner = True
        break
    # User wins by a higher score
    if card_value_user > card_value_dealer:
        print('The Player wins!')
        winner = True
        break
    # Tie
    if card_value_dealer == card_value_user:
        print("It's a tie!")
        winner = True
        break
    
    

    
