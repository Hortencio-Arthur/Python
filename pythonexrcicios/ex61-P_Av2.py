n1 = int(input('Primeiro termo: '))
r = int(input('Razão:'))
ntermos = int(input('Numero de termos: '))
con = 1
termo = n1

while con <= ntermos:
    print(f'{termo} » ', end= ' ')
    con += 1
    termo += r
print('Fim')