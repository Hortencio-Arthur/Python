n = int(input('Digite um numero: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO numero {n} foi divisivel {tot} vezes')

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por issso ele NÂO É PRIMO!')
    