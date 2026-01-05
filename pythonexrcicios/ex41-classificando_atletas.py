from datetime import date
nasc = int(input('Ano de nascimento:'))
ano = date.today().year
idade = ano - nasc

print(f'Um atleta nascido em {nasc} no ano de {ano} tem {idade} anos')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
elif  idade > 25 :
    print('Master')