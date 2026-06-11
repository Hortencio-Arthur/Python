#ler varios numeros, while, e colocar em uma lista X
#mostrar quantos elementos foram digitados
#mostrar ordenar os valores de forma decrescente
#veriificar se tem o numero 5 na lista
#perguntar se quer coninuar, while SN X

lista_numero = []
while True:
    lista_numero.append(int(input('Digite um numero: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break

print('=-' * 30)
print(f'Os valores digitados foram: {lista_numero}')
print(f'Foram digitados [{len(lista_numero)}] elementos.')
print(f'Os valores em ordem decrescente ficam assim: {sorted(lista_numero, reverse=True)}')
if 5 in lista_numero:
    print('O valor [5] esta na lista.')
else:
    print('O valor [5] nao foi digitado.')
