print('=====IDENTIFICADOR DE TRIANGULOS=====')
l1 = float(input('Digite a primeira reta:'))
l2 = float(input('Digite a segunda reta:'))
l3 = float(input('Digite a terceira reta:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('as retas de tamanho {}, {}, {} formam um triangulo'.format(l1, l2, l3))
else:
    print('Essas nao forma um triangulo')