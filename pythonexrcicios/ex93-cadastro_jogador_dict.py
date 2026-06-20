jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))

jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
gols_lista = []
for c in range(jogos):
    gols_lista.append(int(input(f'Quantos gols na partida {c + 1}?: ')))

jogador['gols'] = gols_lista[:]
jogador['total'] = sum(gols_lista)

print('=-' * 30)
print(jogador)

print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k + 1} tem o valor: {v}')

print('=-' * 30)
print(f'Jogador [{jogador["nome"]}] jogou {jogos} jogos.')
for p, g in enumerate(jogador['gols']):
    print(f'  => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
