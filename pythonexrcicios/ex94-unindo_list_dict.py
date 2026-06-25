#cadastrar o nome, sexo, idade, de varias pessoas, usando dicionarios e while
#depois colocar os dicionarios de pessoas em uma lista
# e ao final mostrar:
#   -quantas pessoas foram cadastradas
#   -media de idade
#   -lista com todas as mulheres
#   -lista com pessoas com idade acima da media

cadastros = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/f]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
#calculo media
media = soma_idades =  0
for pessoa in cadastros:
    soma_idades += pessoa['idade']
media = soma_idades / len(cadastros)

#separando as mulheres
mulheres = []
for pessoa in cadastros:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])



print('=-' * 30)
print(f'Foram cadastrados: {len(cadastros)}')
print(f'A Media de todas as idades foi: {media:.1f}')
print(f'As mulheres cadastrasdas foram: {mulheres}')
print('Aquie estao as pessoas acima da media: ')
#pessoas acima da idade media
for pessoa in cadastros:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'   {k} = {v}', end='; ')
        print()
    else:
        print('Nao há pessoas com idade acima da media.')

print('Fim...')