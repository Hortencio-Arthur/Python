estudantes = []
temp = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    temp.append(nome)

    notas = []
    for c in range(2):
        nota = float(input(f'Nota {c + 1}: '))
        notas.append(nota)
    temp.append(notas)

    estudantes.append(temp[:])
    temp.clear()

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

    print('-' * 30)
print('=-' * 40)

print(f'{"No.":<3}', f'{"NOME":<15}', f'{"MEDIA":<3}')
print('-' * 30)
for n, aluno in enumerate(estudantes):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{n:<3}', f'{aluno[0]:<15}', f'{media:<3}')

while True:
        mostrar_notas = int(input('Quer ver as notas de qual aluno? (999) interronpe: '))
        if mostrar_notas == 999:
            break
        if mostrar_notas <= len(estudantes) - 1:
            print(f'As notas de {estudantes[mostrar_notas][0]} sao: {estudantes[mostrar_notas][1]}')
        else:
            print('Aluno invalido. Tente novamente!')

print('FINALIZANDO...')
print('<<<< VOLTE SEMPRE >>>>')