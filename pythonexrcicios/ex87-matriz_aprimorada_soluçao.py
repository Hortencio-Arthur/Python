matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)
spar = mai = scoluna = 0
print('==' * 30 )
for linha in matriz:
    for num in linha:
        print(f'[ {num:^5} ]', end=' ')
        if num % 2 == 0:
            spar += num
    print()

print('==' * 30)
print(f'A soma dos valores pares é: {spar}')
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f'A soma da soma dos valores da terceira coluna é {scoluna}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'O maior valora da segunda linha é : {mai}')