"""pessoas = {
    'nome': 'Arthur',
    'idade': 18,
    'sexo': 'M'
}
#print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
pessoas['peso'] = 100
print(pessoas)
"""
"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP '}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[1]['sigla'])"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
    #    print(f'O campo {k} tem o valor {v}.')
    for v in e.values():
        print(v, end=' ')