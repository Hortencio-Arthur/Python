#adicinar varios valores,while, em uma lista
#perguntar se quer continuar com SN
#mostrar:
#lista com todos os valores
#lista com pares
#lista com impares

lista_numeros = []
while True:
    lista_numeros.append(int(input('Digite um numero: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
lista_pares = []
lista_impares = []
for n in lista_numeros:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print(f'A lista completa é : {lista_numeros}')
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de impares é : {lista_impares}')
