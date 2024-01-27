"""
Создать ф-цию, кот принимаеи список чисел и возвр список чисел, но числа только те, которые делятся на сумму цифр
"""


def division_sum(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % sum([int(i) for i in str(n)]) == 0]


print(division_sum([21, 13]))  # [21]
