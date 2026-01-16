print('=' * 30)
print('     10 termos de uma PA' )
print('=' * 30)

n1 = int(input('Primeiro termo:'))
r = int(input('Razão: '))
dec = n1 + (10 - 1) * r
print(dec)
for c in range(n1,dec+1, r):
    print(c, end = '-> ')
print('Acabou!')