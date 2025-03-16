from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == "__main__":
    circle = Circle(2)
    print(circle.area())
    print(circle.perimeter())

    circle2 = Circle(7)
    print(circle2.area())
    print(circle2.perimeter())
