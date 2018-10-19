import math


class AreaCalculator:
    def calculate(self, shapes):
        area = 0

        for shape in shapes:
            if isinstance(shape, Square):
                area += (shape.width * shape.height)
            if isinstance(shape, Circle):
                area += math.pi * shape.radius ** 2

        return area


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def main():
    square_1 = Square(3, 5)
    square_2 = Square(4, 6)

    circle_1 = Circle(5)
    circle_2 = Circle(7)

    area_calculator = AreaCalculator()
    print(area_calculator.calculate([square_1, square_2, circle_1, circle_2]))


if __name__ == '__main__':
    main()
