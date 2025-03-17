from math import sqrt


class Polygon:
    def __init__(self, n_sides: int, *sides: int):
        self.n_sides = n_sides
        self.sides = sides[:n_sides]


class Triangle(Polygon):
    def __init__(self, *sides):
        super().__init__(3, *sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    print("Triangle 1 area:", t.area())

    t2 = Triangle(10, 15, 9, 10, 12)
    print("Triangle 2 area:", t2.area())
