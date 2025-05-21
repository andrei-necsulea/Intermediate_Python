'''
Create a class named Rectangle. The class should have two fields:
- for the sides
- and the area (property) method to calculate the area of the rectangle.
'''

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width*self.length

    def __str__(self):
        return f"\nArea of {self.__class__.__name__} is : {self.area}"

rectangle_1 = Rectangle(30 , 20)
print(rectangle_1)