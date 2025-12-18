from random import shuffle
alu1 = str(input('primeiro aluno:'))
alu2 = str(input('segundo aluno:'))
alu3 = str(input('terceiro aluno:'))
alu4 = str(input('quarto aluno:'))
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)

print('A ordem da apresentaçao sera {}'.format(lista))