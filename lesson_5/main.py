from math import sqrt


class Square:
    def __init__(self, a1: int):
        self.a: int = a1

    def square_area(self, a2: int | None = None) -> int:
        if a2 is None:
            return self.a * self.a

        else:
            return self.a * a2

    def square_perimetr(self) -> int:
        return (self.a + self.a)*2

    def diagonal(self) -> float:
        return sqrt(self.a**2 + self.a**2)


sq = Square(1)
print(sq.square_area())
print(sq.square_area(4))
