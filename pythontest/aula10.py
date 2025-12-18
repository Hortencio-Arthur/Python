nome = str(input('Qual te seu nome?:')).strip().lower()
if nome == 'arthur':
    print('Que nome legal!')
else:
    print('Que nome diferente!')

print('Bom dia {}'.format(nome.capitalize()))