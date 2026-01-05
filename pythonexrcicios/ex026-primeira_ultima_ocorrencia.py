frase = str(input('Digite uma frase:')).strip().lower()

print('A frase tem {} letras A'.format(frase.count('a')))
print('A letra A aparece primeiro na posiçao {}'.format(frase.find('a')+1))
print('E a ultima aparece na posiçao {}'.format(frase.rfind('a')+1))