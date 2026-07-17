#criar uma lista numeros
#fazer duas funções:
#  sorteia(), sortear 5 numeros e colocar na lista
#  somar_par(), mostrar a soma de todos os valores pares da lista

from random import randint

numeros = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')

    for c in range(5):
        num = randint(1,10)
        print(f'{num},', end=' ')
        lista.append(num)
    print('PRONTO!')

def soma_par(lista):
    print(f'Somando os valores pares de {lista}:', end=' ')

    soma = 0
    for n in lista:
        if n % 2 == 0:
            print(f'[{n}]', end=' ')
            soma += n
    print(f'= {soma}')

sorteia(numeros)
soma_par(numeros)
