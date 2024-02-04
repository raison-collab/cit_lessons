"""
A,B,C - целые числа
"""

for a in range(101, 10000):
    b = a - 10
    c = a + 15

    while b != c:
        if b > c:
            b = b - c
        else:
            c = c - b

    if c == 25:
        print(a)
