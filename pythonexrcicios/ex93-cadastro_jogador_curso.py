jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou?: '))

partidas = list()
for c in range(tot):
    partidas.append(int(input(f'Quantos gols na partida {c}?: ')))

jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('=-' * 30)
print(jogador)

print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}.')
for i, v in enumerate(jogador['gols']):
    print(f'   =>Na partida {i} fez {v} gols.')
print(f'Foi um totas de {jogador["total"]}.')