print('-=' * 5 , 'Sequencia de fibonacci', '-=' * 5)
ter = int(input('Numero de termos: '))
cont = 0
t1, t2 = 0, 1

while cont < ter:
    print(f'{t1} » ', end = ' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
