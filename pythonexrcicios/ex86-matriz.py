#criar uma matriz de 3x3 com valores lidos pelo teclado

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('==' * 30 )
for linha in matriz:
    for num in linha:
        print(f'[ {num:^5} ]', end=' ')
    print()
