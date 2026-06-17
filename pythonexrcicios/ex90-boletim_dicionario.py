nome = str(input('Nome: '))
media = float(input(f'Media do {nome}: '))
aluno = {
    'nome': nome,
    'media': media
}

if media >= 7:
    situacao = 'APROVADO'
elif media >= 5:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'REPROVADO'
aluno['situacao'] = situacao

for chave, valor in aluno.items():
    print(f'{chave.upper()} é igual a [{valor}]')
    