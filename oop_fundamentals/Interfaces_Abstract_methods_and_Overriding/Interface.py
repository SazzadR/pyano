from abc import ABCMeta, abstractmethod


class Shape(object, metaclass=ABCMeta):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

# rectangle = Rectangle(2, 4)
# print(rectangle.area())
# print(rectangle.perimeter())
