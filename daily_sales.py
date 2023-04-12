# Luke Psyhogios, April 17th 2022, Section 001, Assignment 7, Problem #0: Daily Sales

# Make an empty list times seven
weekly_sales = [0]*7

for i in range(len(weekly_sales)):
    # Set conditional variables
    valid = False
    while valid == False:
        daily_sales = int(input('Sales for day ' + str(i+1) + ':'))
        # Ensure daily sales is a valid number
        if daily_sales >=0:
            weekly_sales[i] = daily_sales
            valid = True
        else:
            print("Sorry, that's not valid. Try again.")
# Compute variables for display
total = sum(weekly_sales)
avg = sum(weekly_sales)/len(weekly_sales)
high = max(weekly_sales)
low = min(weekly_sales)
# Display
print('Total sales:', total)
print('Average sales:', round(avg,2))
print('Highest sales day:', high)
print('Lowest sales day:', low)
