class Character:
    def __init__(self, name: str, coordinates: tuple):
        self.name = name
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_name(self) -> str:
        return self.name

    def get_coordinates(self) -> tuple:
        return self.x, self.y


class JohnCharacter(Character):
    def __init__(self, name: str, coordinates: tuple, skill: str):
        super().__init__(name, coordinates)
        self.skill = skill

    def get_skill(self) -> str:
        return self.skill


character = Character("Daniil", (120, 400))

character.get_name()
character.get_coordinates()

danil = Character("danil", (50, 70))

danil.get_name()
danil.get_coordinates()


john_character = JohnCharacter("John", (200, 100), "poison")
