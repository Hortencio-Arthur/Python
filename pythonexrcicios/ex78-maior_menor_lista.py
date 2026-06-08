""""#adicionar 5 valores em uma lista
#depois falar qual é o menor e maior e suas posiçoes
#caso o numero apareça em mais de uma posiçao mostrar as duas
lista_numeros = []
for cont in range(5):
    lista_numeros.append(int(input(f'Digite o °{cont} valor: ')))

maior = menor = 0
for posicao, numero in enumerate(lista_numeros):
    if posicao == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

menor_lis = []
maior_lis = []
for pos, num in enumerate(lista_numeros):
    if num == maior:
        maior_lis.append(pos + 1)
    if num == menor:
        menor_lis.append(pos + 1)

print('=-' * 40)
print(f'Voce digitou os valores: {lista_numeros}')
print(f'O MAIOR valor foi {maior} nas posiçoes {maior_lis}.')
print(f'O MENOR valor foi {menor} nas posiçoes {menor_lis}.')"""

#solucao curso
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor para a posiçao {c}: ')))

    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]

        if listanum[c] < menor:
            menor = listanum[c]


print('=-' * 30)
print(f'Voce digitou os valores: {listanum}')
print(f'O MAIOR valor foi {maior} nas posições: ', end = ' ')
for i , v in enumerate(listanum):
    if v == maior:
        print(f'{i + 1}...', end = ' ')
print()

print(f'O MENOR valor foi {menor}  nas posições: ', end = ' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i + 1}...', end = ' ')
print()
