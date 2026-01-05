'''from datetime import date
nasc = int(input('Digite o ano de nascimento:'))
ano = date.today().year
idade = (ano - nasc)

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano}')
#calculo do alistamentoe
if idade < 18:
    print(f'faltam {ano - idade} anos para o alistamento')
    print(f'Seu alistamento sera em {nasc + 18}')
elif idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade> 18:
    print(f'Você deveria ter se alistado em {nasc + 18}')'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
alist = nasc + 18
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('voce tem que se alistar IMEDITAMENTE!')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    print(f'Seu alistamento sera em {alist} ano')
if idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado ha {saldo} anos')
    print (f'Seu alistamento foi em {alist}')