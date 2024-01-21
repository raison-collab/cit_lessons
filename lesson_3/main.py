def min_max(numbers: list) -> list:
    if not numbers:
        return []

    l = [min(numbers), max(numbers)]

    return l


def main():
    f1 = [1, 465, 56, 123445]
    f2 = [-1231231, 123123, 0, 213123, 34, -40394]
    f3 = []

    print(min_max(f1))
    print(min_max(f2))
    print(min_max(f3))
    print(min_max(f1+f2))


main()
