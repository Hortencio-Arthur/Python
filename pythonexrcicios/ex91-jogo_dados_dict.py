"""from random import randint
jogadores = {}
for c in range(4):
    jogadores[f'jogador{c + 1}'] = randint(1,6)

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou: [{v}]')

print('Rankings dos jogadores: ')
maior = menor = segundo = terceiro = 0
for k, v in jogadores.items():
    if k == 'jogador1':
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
for k,v in jogadores.items():
    if v == maior or v == menor:
        continue
    else:
        if v  > segundo:
            segundo = v
        if v < segundo:
            terceiro = v

print(maior, segundo, terceiro, menor)"""

from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

for k, v in jogo.items():
    print(f'{k} tirou: [{v}] no dado')
    sleep(0.5)
print('=-' * 30)
raking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i +1}° lugal: {v[0]} com {v[1]}.')
    sleep(0.5)













