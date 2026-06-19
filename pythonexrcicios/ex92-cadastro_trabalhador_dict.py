from datetime import date
nome = str(input('Nome: '))
nascimento = int(input('Data de Nascimento: '))
idade = date.today().year - nascimento
clt = int(input('Carteira de Trabalho (0 nao tem): '))
trabalhador = {}
if clt != 0:
    contrat = int(input('Ano de Contratação: '))
    salario = float(input('Salário: R$'))
    aposentadoria = idade + 30

    trabalhador = {'nome': nome, 'idade': idade, 'ctps': clt, 'contrataçao': contrat,
                   'salario': salario, 'aposentadoria': aposentadoria }

else:
    trabalhador = {'nome': nome, 'idade': idade, 'ctps': clt}

for k, v in trabalhador.items():
    print(f'- {k} é igual a {v}.')
