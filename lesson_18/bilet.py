class Bilet:
    def __init__(self, date: int, time: int, place: str, price: int):
        self.date = date
        self.time = time
        self.place = place
        self.price = price

    def is_valid(self):
        return True


class Polet:
    def __init__(self):
        self.bilets = []

    def check_ticket_validity(self, bilet: list):
        if bilet.is_valid():
            return True
        else:
            return False

    def dobavit_bilet(self, bilet: list):
        self.bilets.append(bilet)
        print("Билет успешно добавлен на рейс")

    def ydalit_bilet(self, bilet: list):
        if bilet in self.bilets:
            self.bilets.remove(bilet)
            print("Билет удалён с рейса")
        else:
            print("Билет не найден")


polet = Polet()
bilet1 = Bilet("01.01.2024", "14:00", "Москва - Париж", 1100)
bilet2 = Bilet("02.01.2024", "15:00", "Париж - Москва", 6600)
polet.dobavit_bilet(bilet1)
polet.dobavit_bilet(bilet2)
print("Количество билетов на рейсе:", len(polet.bilets))
polet.ydalit_bilet(bilet1)
print("Количество билетов на рейсе после удаления:", len(polet.bilets))
