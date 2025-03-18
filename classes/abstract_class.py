from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


if __name__ == "__main__":
    rectangle = Rectangle(10, 20)
    circle = Circle(5)

    shapes = [rectangle, circle]

    for shape in shapes:
        print(shape.name, "area:", shape.area())
