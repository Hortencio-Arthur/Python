from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
maior = n1
while op != 5:
    print('1-Somar\n'
          '2-Multiplicar\n'
          '3-Maior\n'
          '4-Novos numeros\n'
          '5-Sair do programa')
    op = int(input('Qual a sua opção?: '))
    if op == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
        print('=' * 15)
    elif op == 2:
        print(f'O resultado entre {n1} * {n2} é {n1 * n2}')
        print('=' * 15)
    elif op == 3:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print(f'O maior entre {n1} e {n2} é {maior}')
        print('=' * 15)
    elif op == 4:
        print('Digite os novos valores.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=' * 15)
    elif op == 5:
        fim = True
        print('Finalizando...')
        print('=' * 15)
    else:
        print('Opção invalida! Tente novamente.')
        print('=' * 15)
    sleep(1)
print('Fim do programa!')