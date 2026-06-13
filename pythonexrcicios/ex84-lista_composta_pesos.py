#ler nome e peso de varia pessoas e colocar em uma lista X
#ao final mostrar:
#quantas pessoas foram cadastradasX
#uma lista gem com as pessoa(s) mais pesadas e uma com as mais leves X
#perguntar se quer continuar SN X

pessoas = []
dados = []
peso_maior = peso_menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        peso_maior = pessoa[1]
        peso_menor = pessoa[1]
    else:
        if pessoa[1] > peso_maior:
            peso_maior = pessoa[1]
        if pessoa[1] < peso_menor:
            peso_menor = pessoa[1]

pesada = []
leve = []
for pessoa in pessoas:
    if pessoa[1] == peso_maior:
       pesada.append(pessoa[0])
    if pessoa[1] == peso_menor:
        leve.append(pessoa[0])
print('=-' * 30)
print(f'Foram cadastradas {len(pessoas)}')
print(f'O maior peso foi de {peso_maior}Kg. Peso de {pesada}')
print(f'O menor peso foi de {peso_menor}Kg. Peso de {leve}')