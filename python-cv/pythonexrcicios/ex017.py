'''co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hip = (co ** 2 + ca ** 2)**(1/2)

print('O valor da hipotenusa  é {}'.format(hip))'''
from math import hypot
co= float(input('Valor do cateto oposto:'))
ca= float(input('Valor do cateto adjacente:'))
hip = hypot(co, ca)

print(hip)

      