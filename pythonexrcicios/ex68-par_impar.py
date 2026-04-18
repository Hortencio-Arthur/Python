"""
X fazer um jogo do par ou impar com o computador
X so é interrompido quando o jogador perde
X mostra o numero de vitorias consecutivas
-
"""
from random import randint
vitoria = True
cont = 0

while vitoria:
    try:
        ncomp = randint(1, 10)
        n = int(input('Digite um numero de 1 a 10: '))
        soma = ncomp + n
    except ValueError:
        print('valor invalido')
        continue
    escolha = input('Escolha PAR ou IMPAR: ').upper().strip()[0]
    if escolha == 'P':
        if soma%2 == 0:
            vitoria = True
            print('VITORIA!!')
            cont += 1
        else:
            vitoria = False
            print('DERROTA!!')
    elif escolha == 'I':
        if soma%2 != 0:
            vitoria = True
            print('VITORIA!!')
            cont += 1
        else:
            vitoria = False
            print('DERROTA!!')
    else:
        print('Resposta invalida tente novamente')
        continue
    print(f'A soma foi {soma}')
print(f'O numero do vitorias consecutivas foi {cont}')
print('Encerrando...')