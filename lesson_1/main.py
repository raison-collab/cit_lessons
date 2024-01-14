def sum_(a: int, b: int) -> str:
    return str(a + b)


l = []
for num in range(2, 50):
    if num % 2 == 0:
        l.append(num)

print(l)

chet = [num for num in range(2, 50) if num % 2 == 0]
print(chet)
