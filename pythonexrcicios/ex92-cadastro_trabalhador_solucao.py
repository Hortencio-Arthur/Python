from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de Nascimento: '))
dados['idade'] = datetime.now().year - nasc #com o datetime.now pega momento exato, hora, milissegundo
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)

print('=-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor = [{v}]')