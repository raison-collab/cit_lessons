import csv


def main():
    with open('data/Book1.csv', encoding='utf8') as file:
        content = csv.reader(file, delimiter=';')

        for row in content:
            for el in row:
                print(el)



main()
