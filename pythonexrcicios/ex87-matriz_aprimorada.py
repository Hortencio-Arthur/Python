#mostrar ao final:
#soma de todos os valores pares digitados
#soma dos valores da terceira coluna
#maior valor da segunda linha

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('==' * 30 )

soma = somacoluna = maior = 0
for l, linha in enumerate(matriz):
    for c, num in enumerate(linha):
        print(f'[ {num:^5} ]', end=' ')

        if num % 2 == 0:
            soma += num
        if c == 2:
            somacoluna += num
        if  linha == matriz[1]:
            if num == linha[0]:
                maior = num
            else:
                if num > maior:
                    maior = num
    print()
print('==' * 30)
print(f'A soma dos valores pares foi [{soma}].')
print(f'A soma do valores nas terceira coluna foi [{somacoluna}].')
print(f'E o Maior valor da segunda linha é [{maior}].')