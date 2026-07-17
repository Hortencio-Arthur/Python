#help(print)
#print(input.__doc__)

"""docstrings
def contador(i,f,p):

    - Faz contage e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')

contador(2, 10, 2)
help(contador)"""

""""parametros opcionais

def somar(a=0, b=0, c=0):
    -Faz a soma de tres valores e mostra o resultado na tela.
    :param a:
    :param b:
    :param c:
    :return:
    
    s = a + b + c
    print(f'A soma vale {s}.')

somar(3, 2, 5)
somar(8,4)
somar()
somar(b=4, c=6)
somar(c=2, a=3)"""

"""" escopo de funcoes, global/local
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}')
#programa principal
n = 2
print(f'No programa principal, n vale {n}.')
teste()
print(f'No programa principal, x vale {x}')

def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')
n1 = 2
print(f'n1 fora vale {n1}')
funcao()"""

def somar(a=0, b =0, c=0):
    s = a + b + c
    return s
r1 = somar( 3, 2 , 5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2}, {r3}.')