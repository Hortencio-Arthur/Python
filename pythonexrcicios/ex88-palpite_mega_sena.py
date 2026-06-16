#perguntar quantos jogos serao jogados
#sortear 6 numero ente 1 e 60 para cada jogo
#cadastrar os numeros em uma linha composta
from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
quantidade_jogos = int(input('Quantos jogos voce vai joga?: '))
print(f'{f" SORTEANDO {quantidade_jogos} JOGOS ":=^30}')

#versao com listas simples
""""jogos = []
for c in range(1, quantidade_jogos + 1):
    while len(jogos) < 6:
        sorteio = randint(1, 60)
        if sorteio not in jogos:
            jogos.append(sorteio)
    jogos.sort()
    print(f'Jogo {c}: {jogos}')
    jogos.clear()
    sleep(0.5)"""

#vesao com lista composta
jogos = []
temp = []
for c in range(1, quantidade_jogos + 1):
    while len(temp) < 6:
        sorteio = randint(1, 60)
        if sorteio not in temp:
            temp.append(sorteio)
    temp.sort()
    jogos.append(temp[:])
    temp.clear()

for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')
    sleep(0.5)

print(f'{"< BOA SORTE! >":=^30}')