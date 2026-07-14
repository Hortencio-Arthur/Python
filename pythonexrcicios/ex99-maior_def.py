#criar funçao chamada maior()
#recebe vairo parametros inteiros

def maior(* num):
    print('=-' * 30)
    print('Analisando os valores passados...')


    print('Valores: ', end='')
    num_maior = 0
    for cont, valor in enumerate(num):
        print(f'{valor}', end=' ')

        if cont == 0:
            num_maior = valor
        else:
            if valor > num_maior:
                num_maior = valor

    print()
    print(f'Foram informados [{len(num)}] valores.')
    print(f'O maior valor informado foi [{num_maior}]')


maior(1,2,3)
maior(0)
maior(1, 4, 2, 9, 5)
maior(123, 32, 12222, 2)
maior()
maior(-10, -5, -100)