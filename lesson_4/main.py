"""
Написать ф-цию(список), кот везвращает True если список отсортирован, в ином случае False
"""


def check_sort_list(l: list):
    sorted_list = sorted(l)
    if l == sorted_list:
        return True
    return False


print(check_sort_list([1, 4, 3]))
