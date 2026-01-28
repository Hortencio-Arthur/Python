'''n = int(input('Digite um numero para calcular o fatorial: '))
f = 1

while n > 0:
    print(f'{n}', end=' ')
    print('X ' if n > 1 else '= ', end = ' ')
    f *= n
    n -= 1

print(f)'''
'''from math import factorial
n = int(input('Digite um numero para calcular fatorial: '))
f  = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n = int(input('Digite um numero para calcular o fatorila: '))
c = n
f = 1
print(f'Calculando {n}! =', end= ' ')

while c > 0:
    print(f'{c} ', end = ' ')
    print(' X ' if c > 1 else ' = ', end = ' ')
    f *= c
    c -= 1
print(f )