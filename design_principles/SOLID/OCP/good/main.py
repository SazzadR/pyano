import math
from abc import ABCMeta, abstractmethod


class ShapeInterface(metaclass=ABCMeta):
    @abstractmethod
    def area(self): pass


class AreaCalculator:
    def calculate(self, shapes):
        area = 0

        for shape in shapes:
            area += shape.area()

        return area


class Square(ShapeInterface):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def main():
    square_1 = Square(3, 5)
    square_2 = Square(4, 6)

    circle_1 = Circle(5)
    circle_2 = Circle(7)

    area_calculator = AreaCalculator()
    print(area_calculator.calculate([square_1, square_2, circle_1, circle_2]))


if __name__ == '__main__':
    main()
