""""teste = list()
teste.append('Arthur')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 18
galera.append(teste[:])
print(galera)"""

""""galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
print(galera)
print(galera[3][1])
for p in galera:
    print(f'nome: {p[0]}, idade: {p[1]}')"""

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digire a sua idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'temos {totmai} maiores e {totmen} menores de idade.')