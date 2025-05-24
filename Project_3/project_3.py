'''
On the basis of the abstract class Polygon, create 3 child classes: Square, Rectangle, Triangle.
Each of these classes must be concrete (not abstract), so it should override all abstract methods in the Polygon class. Each specific class should have a __init__ constructor definition (for example, an object of the Square type, should have one self.side attribute, a Rectangle object should have two attributes: self.side1, self.side2, and Triangle self.side, self.height).

Finally, create an object management function for the created classes, which in the loop will calculate the fields for every object.
'''

from abc import ABC, abstractmethod
from typing import Union


class Polygon(ABC):
    @abstractmethod
    def count_field(self) -> Union[int, float]:  # Union suggests that the function might return an int or a float
        """The method is to calculate the area of a given object.
         Due to the fact that we do not know what a polygon is at the moment,
         we can't calculate its field. To be redefined in the inheriting class.
         :return: The value of the field as an integer or rational number.
        """
        pass


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def count_field(self) -> Union[int, float]:
        return self.side**2


class Rectangle(Polygon):
    def __init__(self, side1 , side2):
        self.side1 = side1
        self.side2 = side2

    def count_field(self) -> Union[int, float]:
        return self.side1 * self.side2


class Triangle(Polygon):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def count_field(self) -> Union[int, float]:
        return (self.side * self.height)/2


def count_fields(polygons: list) -> list:
    """Calculates the area of all polygons given in the list.
     :param polygons: list of objects inheriting Polygon.
     :return: list of computed poles.
    """
    object_area = []
    for object_iterator in  polygons:
        object_area.append(object_iterator.count_field())
    return object_area


square_1 = Square(20)
rectangle_1 = Rectangle(10, 20)
triangle_1 = Triangle(30, 10)

poligoane = [square_1, rectangle_1, triangle_1]

print(count_fields(poligoane))