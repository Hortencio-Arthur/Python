from time import sleep
def contador(i, f, p):
    print('=-' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.5)
    else:
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)

    print('FIM!')

#programa principal
contador(1,10, 1)
contador(10, 0, 2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)