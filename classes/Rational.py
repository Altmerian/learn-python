class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return f"{self.p}/{self.q}"

    def __add__(self, other):
        return Rational(self.p * other.q + other.p * self.q, self.q * other.q)

    def __sub__(self, other):
        return Rational(self.p * other.q - other.p * self.q, self.q * other.q)


if __name__ == "__main__":
    r1 = Rational(2, 3)
    r2 = Rational(1, 2)
    print(f"{r1} + {r2} = {r1 + r2}")
    print(f"{r1} - {r2} = {r1 - r2}")
