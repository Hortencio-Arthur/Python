print('==ANALISADOR DE TRIANGULOS==')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print(f'As retas {l1}, {l2}, {l3} formam um tringulo', end='')
    if l1 == l2 ==l3:
        print('Equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isosceles')
    elif l1 != l2 != l3 != l1:
        print('Escaleno')
else:
    print(f'As retas {l1}, {l2}, {l3} nao formam um tringulo')
