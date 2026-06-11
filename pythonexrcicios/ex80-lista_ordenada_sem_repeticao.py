""""#adicionar 5 valores em uma lista
#adicionar em ordem sem sort
#mostrar a posiçao do indice do valor

numeros_lista = []
for c in range(5):
    numero = (int(input(f'Digite o seu {c + 1}° numero: ')))
    if c == 0 or numero > numeros_lista[-1]:
        numeros_lista.append(numero)
        print(f'O numero foi adicionado no final da lista.')
    else:
        for pos, n in enumerate(numeros_lista):
            if numero <= n:
                numeros_lista.insert(pos, numero)
                print(f'O numero foi adicionado na posiçao {pos}.')
                break

print('=-' * 30)
print(f'Sua lista ficou assim: {numeros_lista}')
"""
# curso
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        #original
        """" pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'o valor foi adicionado na posiçao {pos}')
                break
            pos += 1"""
        #teste com for
        for pos, num in enumerate(lista):
            if n <= num:
                lista.insert(pos, n)
                print(f'o valor foi adicionado na posiçao {pos}')
                break

print('=-' * 30)
print(f'os valores em ordem ficam assim: {lista}')









