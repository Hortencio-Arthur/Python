'''from random import randint

print('JOGO DA ADIVINHAÇÃO V2')
num = int(input('Qual o seu palpite de um numero de 0 a 10: '))
sort = randint(0,10)
tenta = 1

while num != sort:
    tenta += 1
    if num < sort:
        num = int(input('Mais.tente novamente: '))
    else:
        num = int(input('Menos.Tente novamente: '))
print(f'Acerotu com {tenta} tentativas! parabens!')'''

from random import randint
computador = randint(0, 10)
print('Eu sou o seu computador...'
      ''
      'Acabei de pensar em um numero entre 0 e 10.'
      'Sera que vo consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez: ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez: ')
print(f'Acertou com {palpite}  tentativas!')
