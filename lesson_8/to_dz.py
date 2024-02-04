class Student:
    def __init__(self, name: str, group: str):
        """
        Класс, описывающий студента
        :param name: Имя студента
        :param group: Группа обучения (буква класса, например, "А")
        """
        self.name = name
        self.group = group

    def study(self):
        print(f'Я, {self.name}, Учусь в группе {self.group}')


class Teacher:
    def __init__(self, name: str, subject: str):
        """
        Класс, описывающий учителя
        :param name: Имя учителя
        :param subject: Предмет, который преподает учитель
        """
        self.name = name
        self.subject = subject

    def teach(self):
        return f'Меня зовут {self.name}, я - учитель по дисциплине "{self.subject}"'


class School:
    def __init__(self, name: str, students: list[str], teachers: list[str]):
        """
        Класс, описывающий школу
        :param name: Название школы
        :param students: список студентов (их имен)
        :param teachers: список учителей (их имен)
        """
        self.name = name
        self.students = students
        self.teachers = teachers

    def get_school_info(self, address: str) -> dict:
        """
        Возвращает информацию о школе
        :param address: Адрес школы
        :return: Словарь с информацией
        """
        data = {
            'school': {
                'name': self.name,
                'address': address
            },
            'teachers': self.teachers,
            'students': self.students
        }
        return data

