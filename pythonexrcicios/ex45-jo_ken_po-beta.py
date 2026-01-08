from random import choice
print('PEDRA PAPEL TESOURA')
print('''
Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogada = int(input('Qual a sua jogada?'))
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
sorteio = choice(jokenpo)

if jogada == 0:
    jogada = str('PEDRA')
elif jogada == 1:
    jogada = str('PAPEL')
elif jogada == 2:
    jogada = str('TESOURA')
else:
    print('jogada invalida! tente novamente')

print(f'Computador jogou {sorteio}')
print(f'Jogador jogou {jogada}')

if jogada == sorteio:
    print('EMPATE')

