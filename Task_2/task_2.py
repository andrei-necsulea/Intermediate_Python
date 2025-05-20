'''
Create a Rectangle class whose attributes will be the height and width of the figure.
Implement methods to measure the perimeter and area of a rectangle.
Then create a Square class, remembering that every square is a rectangle,
but not every rectangle is a square.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length*self.width

    def __str__(self):
        return f"\nPerimeter of {self.__class__.__name__} is : {self.perimeter()}\nArea of {self.__class__.__name__} is : {self.area()}"

class Square(Rectangle):
    def __init__(self , length):
        super().__init__(length , length)

rectangle_1 = Rectangle(20 , 30)
square_1 = Square(20)

print(rectangle_1)
print(square_1)