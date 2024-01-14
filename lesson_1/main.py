def average(numbers: list | tuple) -> int | float:
    """
    Среднее ариф
    :param numbers: список чисел
    :return: число
    """

    ans = sum(numbers) / len(numbers)

    return ans


print(average([1, 2, 3, 4, 5]))
