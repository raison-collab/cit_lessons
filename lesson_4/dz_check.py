def f(numbers: list[int]) -> list[int]:
    """
    1) пробежкаться по numbers
    2) проверить на чет
    3) если чет, то возв в квадрат
    4) добавить это число в новый список
    5) вернуть список
    """
    l = []

    for num in numbers:
        if num % 2 == 0:
            l.append(num ** 2)

    return l


print(f([1, 2, 3, 4, 5]))
