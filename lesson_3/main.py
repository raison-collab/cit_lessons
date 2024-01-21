def reverse_string(text: str) -> str:
    t = reversed(text)
    return ''.join(t)


def main():
    f1 = 'hello'
    f2 = 'world'

    print(reverse_string(f1))
    print(reverse_string(f2))
    print(reverse_string(f1+f2))


main()
