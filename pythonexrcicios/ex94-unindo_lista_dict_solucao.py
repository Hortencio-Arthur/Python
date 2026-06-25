pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa.clear()
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        res = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        if res in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if res == 'N':
        break

print('=-' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')

print('C) As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()

print('D) Lista das pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
        
print('<<<Encerrado>>>')

