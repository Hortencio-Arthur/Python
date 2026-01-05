'''nome = str(input('Digite o seu nome completo: ')).strip()

print('seu primeiro nome é {} e o seu ultimo é {}'.format(nome.split()[0], nome.split()[-1]))'''

n = str(input('digite o seu nome completo: ')).strip()
nome= n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))