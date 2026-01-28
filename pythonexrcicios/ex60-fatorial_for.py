n = int(input('Digit e um numero para calcular o fartorial: '))
f = 1
for c in range(1, n + 1):
    print(f'{n} ', end=' ')
    print(' X ' if n > 1 else ' = ', end=' ')
    f *= n
    n -= 1

print(f)