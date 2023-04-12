# Luke Psyhogios, March 28th 2022, Section 001, Problem #0, Challenge 1: Simple Functions

# Function: maximum
# Input: num1 (number), num2 (number)
# Processing: Compares two numbers and returns the larger
# Output: larger number 
def maximum(num1, num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2

# Function: minimum
# Input: num1 (number), num2 (number)
# Processing: Compares two numbers and returns the smaller
# Output: smaller number
def minimum(num1, num2):
    if num1<num2:
        return num1
    elif num2<num1:
        return num2

# Test code
a = 5
b = 10
c = 15
d = 20
ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20
ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5
ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
