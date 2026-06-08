""""#ler quatro valores guardar em uma tupla
#mostrar quantas vezes apareceu o valor 9
#em que posiçao aparece o primeiro 3
#quais os numeros pares


while True:
    numeros = []
    for c in range(4):
        n = int(input(f'Digite o °{c + 1} valor: '))
        numeros.append(n)

    print('==' * 30)
    tupla_numeros = tuple(numeros)
    print('===Analise dos valores===')

    print(f'Numero de 9 dentro dos valores: {tupla_numeros.count(9)}')

    if 3 in tupla_numeros:
        print(f'O numero 3 aparece primeiro na posiçao: {tupla_numeros.index(3) + 1}')
    else:
        print('Nenhum valor 3 foi digitado.')
    print('E os numeros pares que aparecem sao: ', end = ' ')

    for num in tupla_numeros:
        if num % 2 == 0:
            print(f'{num}', end = ' ')
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('\nQuer continuar?: ').strip().upper()[0]
    if resposta == 'N':
        break"""

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite ultimo numero: ')))
print(f'Voce digitou os numeros: {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3) + 1} posiçao.')
else:
    print('Nenhum valor 3 foi digitado.')
print('Os numeros pares foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')