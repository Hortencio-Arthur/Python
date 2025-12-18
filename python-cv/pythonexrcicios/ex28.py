from random import randint
from time import sleep
print('=====JOGO DA ADIVINHAÇAO=====')

num = str(input('Digite um numero de 0 á 5: '))
aleatorio= randint(0,5)
print('CARREGANDO.....')
sleep(2)
if num == aleatorio:
    print('*!' * 10)
    print('ARCETOU!!! FLAMENGOOOOOOOOOOOO')
    print('*!' * 10)
else:
    print('ERROOOOOU RUDE, ERA {} !!! '.format(aleatorio))