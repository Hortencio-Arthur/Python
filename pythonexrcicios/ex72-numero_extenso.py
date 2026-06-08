numeros_extensos = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
                    'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze','doze', 'treze', 'quatorze', 'quinze',
                    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

""""while True:
    try:
        numero_usuario = int(input('Digite um numero entre 0 e 20: '))
        if numero_usuario == 99:
            break
        if 0 <= numero_usuario <= 20:
            print(f'Voce digitou o numero [{numeros_extensos[numero_usuario]}]')
        else:
            print('Valor inválido! Tente novamente.')

    except ValueError:
        print('Valor invalido! Tente novamente.')
        continue
"""
#versao do curso
while True:
    while True:
        try:
            numero = int(input('Digite um numero entre 0 e 20: '))
        except ValueError:
            print('Valor invalido! Prescisa ser um numero.', end=' ')
            continue
        if 0 <= numero <= 20:
            break
        print('Tente novamente.', end = ' ')

    print(f'voce digitou o numero [{numeros_extensos[numero]}].')

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar?: ').strip().upper()[0]

    if resposta == 'N':
        break
print('Encerrando...')