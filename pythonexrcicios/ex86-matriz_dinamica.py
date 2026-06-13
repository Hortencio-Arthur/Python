linhas = int(input('Quantas linhas vai ter sua matriz?: '))
colunas = int(input('Quantas colunas vai ter sua matriz?: '))

matriz = []
for linha in range(0, linhas):
    matriz.append([])
    for coluna in range(0, colunas):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('==' * 30)
for linha in matriz:
    for num in linha:
        print(f'[{num:^5}]', end=' ')
    print()
