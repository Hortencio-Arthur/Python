"""
-ler idade e sexo de varias pessoas X
- a cada pessoa o programa pergunta se quer continuarX
- ao final mostrar:
    quantidade de pessoas com mais de 18 anos,x
    quantidade de homens,x
    quanitdade de mulheres com menos de 20 anosX
"""
print('--CADASTRE UMA PESSOA--')
tot18 = totm = totf =totf20 = cont = soma = 0
while True:
    cont += 1
    print(f'#Cadastro N:{cont}')

    try:
        idade = int(input('Idade: '))
    except ValueError:
        print('Valor invalido. tente novamente.')
        cont -= 1
        continue
    soma += idade
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]

    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    elif sexo == 'F':
        totf += 1
        if idade < 20:
            totf20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
media = soma / cont
print(f'Foram cadastrados {cont} pessoas, dentre qual:\n'
      f'{tot18} tem mais de 18 anos, \n'
      f'{totm} sao homens,\n'
      f'{totf} sao mulheres e {totf20} tem menos de 20 anos.')
print(f'A media de idade de todas as pessoas cadastradas é {media}')
print('Encerrando...')
