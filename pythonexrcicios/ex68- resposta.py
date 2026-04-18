from random import randint
v = 0
while True:
    try:
        jogador = int(input('Digite um valor entre 0 e 10: '))
    except ValueError:
        print('Valor invalido. tente novamente.')
        continue
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}.', end = ' ')
    print('Deu par!' if total % 2 == 0 else 'Deu impar!')
    if tipo == 'P':
        if  total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Voce ganhou {v} vezes.')