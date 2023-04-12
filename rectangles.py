# Luke Psyhogios, May 9th 2022, Section 001, Assignment 11, Problem #0: Rectangles

# Set up class
class Rectangle:
    def __init__(self,w,l,x,y):
        self.width = w
        self.length = l
        self.xpos = x
        self.ypos = y
    # Get the area 
    def get_area(self):
        return self.length*self.width
    # Get the perimeter
    def get_perimeter(self):
        return 2*self.length + 2*self.width

rectangle1 = Rectangle(10,15,5,3)
rectangle2 = Rectangle(3,5,15,7)

print("Rectangle #1")
r1a = rectangle1.get_area()
r1p = rectangle1.get_perimeter()
print('* Coordinates: (', rectangle1.xpos, ',', rectangle1.ypos, ')', sep = '')
print('* Area:', r1a)
print('* Perimeter:', r1p)

print("Rectangle #2")
r2a = rectangle2.get_area()
r2p = rectangle2.get_perimeter()
print('* Coordinates: (', rectangle2.xpos, ',', rectangle2.ypos, ')', sep = '')
print('* Area:', r2a)
print('* Perimeter:', r2p)
