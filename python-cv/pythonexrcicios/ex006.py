'''n = int(input('Digite um numero:'))
D = n*2
T = n*3
R = n**(1/2)

print('o dobro dele é: {}'.format(D))
print( 'o triplo dele é: {}'.format(T))
print( 'a raiz quadrada dele é: {}'.format(R))'''

n = int(input('Digite um numero: '))

print('o dobro do valor {} é {}, \nseu triplo é {}, \ne sua raiz quadrada é {:.3f}'. format(n, (n*2), (n*3), (n**(1/2))))
