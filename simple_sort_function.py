# Luke Psyhogios, March 28th 2022, Section 001, Problem #0, Challenge 3: Simple Functions


# Function: simple_sort_version
# Input: num1 (number), num2 (number), num3 (number)
# Processing: Compares three numbers and returns them in ascending order
# Output: numbers in ascending ordern
def simple_sort_version(num1, num2, num3):
    if num1>num2 and num1>num2:
        if num2>num3:
            return num3, num2, num1
        if num3>num2:
            return num2, num3, num1
    if num2>num1 and num2>num3:
        if num1>num3:
            return num3, num1, num2
        if num3>num1:
            return num1, num3, num2
    if num3>num1 and num3>num2:
        if num1>num2:
            return num2, num1, num3
        if num2>num1:
            return num1, num2, num3
    if num1 == num2:
        if num3>num1:
            return num3, num1, num2
        if num1>num3:
            return num3, num2, num1
    if num1 == num3:
        if num2>num1:
            return num3, num1, num2
        if num1>num2:
            return num2, num3, num1
    if num2 == num3:
        if num1>num2:
            return num3, num2, num1
        if num2>num1:
            return num1, num3, num2

# Test code
a,b,c = simple_sort_version(10,20,30)
print (a,b,c) # 10 20 30
a,b,c = simple_sort_version(10,30,20)
print (a,b,c) # 10 20 30
a,b,c = simple_sort_version(30,20,10)
print (a,b,c) # 10 20 30
a,b,c = simple_sort_version(30,20,20)
print (a,b,c) # 20 20 30

