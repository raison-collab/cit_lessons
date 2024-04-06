"""
Геометрические фигуры

мы ищем площадь и периметр фигур (квадрат, прямоугольник, треугольник)

"название (через аргумент) - периметр (флот) - площадь (флот)"
"""


class Kvadrat:
    def __init__(self, a: float, name: str):
        self.storona = a
        self.nazvanie = name

    def perim(self) -> float:
        return self.storona + self.storona + self.storona + self.storona

    def ploshad(self) -> float:
        return self.storona * self.storona

    def info(self) -> str:
        return f"{self.nazvanie} - {self.perim()} - {self.ploshad()}"


kv = Kvadrat(1.3, "Квадрат 112")
print(kv.info())


class Pryamoug:
    def __init__(self, a: float, b: float, name: str):
        self.storona1 = a
        self.storona2 = b
        self.nazvanie = name

    def perim(self) -> float:
        return (self.storona1 + self.storona2)*2

    def ploshad(self) -> float:
        return self.storona1 * self.storona2

    def info(self) -> str:
        return f"{self.nazvanie} - {self.perim()} - {self.ploshad()}"


pr = Pryamoug(1.2, 2.7, "прямоугольник 550")
print(pr.info())


class Treug:
    def __init__(self, a: float, vysota: float, name: str):
        self.storona = a
        self.vysota = vysota
        self.nazvanie = name

    def ploshad(self) -> float:
        return self.storona * self.vysota / 2

    def info(self) -> str:
        return f"{self.nazvanie} - {self.ploshad()}"


tr = Treug(1.2, 8.7, "треугшольник !!!0")
print(tr.info())
