import datetime
import time


class Product:
    def __init__(self, name: str, price: float, kolizestvo: int):
        self.name = name
        self.price = price
        self.kolizestvo = kolizestvo


class Cklad:
    def __init__(self):
        self.products = []

    def dobavit_product(self, products: list[Product]):
        for el in products:
            self.products.append(el)

    def total_stoumost(self) -> int | float:
        total = 0
        for product in self.products:
            total += product.price * product.kolizestvo
        return total

    def total_stoumost_2(self) -> int | float:
        return sum([product.price * product.kolizestvo for product in self.products])


cklad = Cklad()

product1 = Product("Apple", 7.50, 100)
product2 = Product("Banana", 0.79, 900)
product3 = Product("Banana", 0.79, 900)
product4 = Product("Banana", 0.79, 900)
product5 = Product("Banana", 0.79, 900)
product6 = Product("Banana", 0.79, 900)
product7 = Product("Banana", 0.79, 900)
product8 = Product("Banana", 0.79, 900)
product9 = Product("Banana", 0.79, 900)

start = time.time()
cklad.dobavit_product(
    [product1,
     product2,
     product3,
     product4,
     product5,
     product6,
     product7,
     product8,
     product9]
)

cklad.dobavit_product(
    [
        product1
    ]
)

print(len(cklad.products))

print("Общая стоимость товаров на складе:", cklad.total_stoumost())
print("Общая стоимость товаров на складе:", cklad.total_stoumost_2())
