from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções sao:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')

print('-=' * 11)
print(f'Computador jogou {itens[computador]} ')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32mGANHOU\033[m')
    elif jogador == 2:
        print('\033[1;31mPERDEU\033[m')
    else:
        print('Jogada invalida! Digite 0, 1 ou 2.')
elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('\033[1;31mPERDEU\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;32mGANHOU\033[m')
    else:
        print('Jogada invalida! Digite 0, 1 ou 2.')
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('\033[1;32mGANHOU\033[m')
    elif jogador == 1:
        print('\033[1;31mPERDEU\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE\033[m')
    else:
        print('Jogada invalida! Digite 0, 1 ou 2')