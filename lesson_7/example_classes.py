class Person:
    def __init__(self, name: str, age: int):
        """
        Класс, который описывает человека
        :param name: Имя
        :param age: Возраст
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Приветствие
        :return:
        """
        print(f'Привет, меня зовут {self.name}. Мне {self.age} лет')


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float):
        """
        Класс, который описывает рабочего
        :param name: Имя
        :param age: Возраст
        :param salary: Зарплата
        """
        super().__init__(name, age)
        self.salary = salary

    def annual_salary(self) -> float:
        """
        Считает Зарплату за год
        :return: Зп за год
        """
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float):
        """
        Класс, который описывает менеджера
        :param name: Имя
        :param age: Возраст
        :param salary: Зарплата
        """
        super().__init__(name, age, salary)

    def give_raise(self, percent: float):
        """
        Меняет зарплату на определенный процент
        :param percent: процент
        :return:
        """
        self.salary += self.salary * percent / 100
