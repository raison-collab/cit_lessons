from math import sqrt


def square_area(a1: int, a2: int):
    return a1 * a2


def square_perimetr(a1: int, a2: int):
    return (a1+a2)*2


def diagonal(a1: int, a2: int) -> float:
    return sqrt(a1**2 + a2**2)


print(square_area(1, 4))
print(square_perimetr(1, 4))
print(diagonal(1, 4))


class Square:
    def __init__(self, a1: int, a2: int):
        self.a: int = a1
        self.b: int = a2

    def square_area(self) -> int:
        return self.a * self.b

    def square_perimetr(self) -> int:
        return (self.a + self.b)*2

    def diagonal(self) -> float:
        return sqrt(self.a**2 + self.b**2)


sq = Square(1, 4)
print(sq.square_area())
print(sq.square_perimetr())
print(sq.diagonal())
