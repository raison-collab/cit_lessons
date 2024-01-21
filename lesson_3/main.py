def even_numbers(numbers: list[int]) -> list[int]:
    l = []

    for num in numbers:
        if num % 2 == 0:
            l.append(num)

    return l


def main():
    f1 = [1, 2, 3, 4, 54]
    f2 = [3, 5, 1]
    f3 = []

    print(even_numbers(f1))
    print(even_numbers(f2))
    print(even_numbers(f3))
    print(even_numbers(f1+f2))



main()
