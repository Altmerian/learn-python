class Angle:
    def __init__(self, degree):
        self.degree = degree

    def __add__(self, other):
        return Angle(self.degree + other.degree)

    def __str__(self):
        return f"{self.degree} degrees"


if __name__ == "__main__":
    angle1 = Angle(30)
    angle2 = Angle(45)
    angle3 = angle1 + angle2
    print(angle3)
