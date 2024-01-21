def in_range(numbers: list, start: int, end: int) -> list:
    interval = [num for num in range(start, end+1)]

    l = []

    for num in numbers:
        if num in interval:
            l.append(num)

    return l


def main():
    f1 = in_range(list(range(100)), 96, 105)
    f2 = in_range([4, 7, 9, 124, 12], 5, 15)

    print(f1)
    print(f2)


main()
