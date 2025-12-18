n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))

#verificando o menor o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

#verificando o maior
maior = n1
if n2>n1 and n2>n3:
    maior  = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''if n1 > n2 and n1 > n3:
    print('O numero {} é maio que {} e {}'.format(n1, n2, n3))

if n2 > n1 and n2 > n3:
    print('O numero {} é maior que {} e {}'.format(n2, n1, n3))

if n3 > n1 and n3 > n2:
    print('O numero {} é maior que {} e {}'.format(n3, n1,n2))'''