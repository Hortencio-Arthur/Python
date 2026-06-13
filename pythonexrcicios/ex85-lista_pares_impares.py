#adicionar 7 valores em uma lista unica
# separar os valores em impares e pares dentro da lista
#mostrar os pares e impares em ordem crescente

numeros = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}o valor: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('=' * 40)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os vlaores impares digiados foram: {sorted(numeros[1])}')