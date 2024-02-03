"""
A
B
C
D
"""

n1 = 0
n2 = 0

k = 0

for a1 in 'ABCD':
    for a2 in 'ABCD':
        for a3 in 'ABCD':
            for a4 in 'ABCD':
                for a5 in 'ABCD':
                    word = a1 + a2 + a3 + a4 + a5

                    if word == 'ADCDB':
                        n1 = k

                    elif word == 'BDCDA':
                        n2 = k

                    k += 1

print(n2-n1)
