# Luke Psyhogios, February 9th 2022, Section 001, Problem #0: Lottery Winnings Calculator (Warm-Up)

# Ask user questions about lottery
Winnings = float(input('How much money did you win? '))
People = int(input('How many people are splitting the winnings? ')) 
Tax = float(input('What is the tax rate on winnings? (i.e. 25 = 25%): '))

# Get money variables needed for printing
earnings_per_person = Winnings/People
tax_per_person = earnings_per_person*(Tax/100)
take_home_amount_per_person = earnings_per_person-tax_per_person

# Format variables for printing
earnings_format = '$'+format(Winnings, ',.2f')
earnings_per_person_format = '$'+format(earnings_per_person,',.2f')
tax_per_person_format = '$'+format(tax_per_person,',.2f')
take_home_per_person_format = '$'+format(take_home_amount_per_person,',.2f')

# Print info for user
print()
print('In total you won', earnings_format)
print('Split', People, 'ways that amounts to', earnings_per_person_format, 'per person')
print('Tax per person:', tax_per_person_format)
print('Take home amount per person:', take_home_per_person_format)
