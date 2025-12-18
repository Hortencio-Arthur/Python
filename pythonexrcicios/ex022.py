nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('o seu nome em letras mauscula é {}'.format(nome.upper()))
print('o seu nome em letras minusculas é {}'.format(nome.lower()))
print('O seu nome, sem contar espaços, tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
"""semespaço = nome.replace(' ', "")
print('o seu nome, sem contar espaços, tem {} letras'.format(len(semespaço)))"""
"""primeiro = nome.split()
print('o seu primeiro nome é {} e ele tem {} letras'.format(primeiro[0], len(primeiro[0])))"""