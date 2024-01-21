import json


def main():
    with open('data/data.json') as file:
        content: dict = json.loads(file.read())

    name = content['name']
    family = content['family']

    family_names = [el['name'] for el in family]

    print(family_names)


main()
