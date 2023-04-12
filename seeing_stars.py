# Luke Psyhogios, February 28th 2022, Section 001, Problem #0: Seeing Stars

# Use to check if num1 is positive
condition1 = False

while condition1 == False:
    # get a number
    num1 = int(input('Number 1: '))
    # if it's negative, try again
    if num1<=0:
        print('Invalid, try again!')
    else:
        condition1 = True

# check if number 2 is positive and > num1
condition2 = False

while condition2 == False:
    num2 = int(input('Number 2: '))
    if num1>=num2 or num2<=0:
        print('Invalid, try again!')
    else:
        condition2 = True

# part 2
star = num1
while num2>=star:
    print(star, star*'*')
    star += 1
    
# part 3
star_back = num2 - 1
while num1 <= star_back:
    print(star_back, star_back*'*')
    star_back -= 1

               
               
               

    
