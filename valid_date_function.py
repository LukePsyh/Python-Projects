# Luke Psyhogios, March 28th 2022, Section 001, Problem #0, Challenge 2: Simple Functions

# Function: valid_date
# Input month (integer), day (integer)
# Processing: Evaluates the two inputs to deicde whether the month/day combination is real or not
# Output: Boolean
def valid_date(month, day):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day>31 or day<1:
            return False
        else:
            return True
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day>30 or day<1:
            return False
        else:
            return True
    if month == 2:
        if day>28 or day<1:
            return False
        else:
            return True
    if month>12 or month<1:
        return False
    
# Test Code
print (valid_date(99,1)) # False
print (valid_date(1,99)) # False
print (valid_date(99,99)) # False
print (valid_date(-99,1)) # False
print (valid_date(1,-99)) # False
print (valid_date(-99,-99)) # False
print (valid_date(9,25)) #True
print (valid_date(10,15)) # True
print (valid_date(11,31)) # False
print (valid_date(2,28)) # True
print (valid_date(2,29)) # False
