n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
cont = 1
termo = n1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} » ', end='')
        cont += 1
        termo += r
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais?: '))
print('Fim!')
print(f'Progressao finalizada com {total} termos')

