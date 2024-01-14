def average(numbers: list | tuple) -> int | float:
    """
    Среднее ариф
    :param numbers: список чисел
    :return: число
    """

    ans = sum(numbers) / len(numbers)

    return ans


print(average([1, 2, 3, 4, 5]))


# Проверить поле на то, чтобы в нем было только одно слово

def split_words(text: str) -> list:
    words: list[str] = text.split()
    return words


words = split_words('ПРивет Арсений и Даниил сегодня занятие')
print(words, len(words))
