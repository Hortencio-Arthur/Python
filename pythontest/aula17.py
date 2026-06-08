""""num = [2, 5, 9, 1]
print(num)
num[3] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse = True)
print(num)
num.insert(2, 0)
print(num)
print(f'essa lista em {len(num)} elementos.')
num.pop(2)
print(num)
if 4 in num:
    num.remove(4)"""

num = []
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
#for v in num:
  #  print(f'{v}...', end='')

for c, v in enumerate(num):
    print(f'Na posicao {c} encontrei o valor {v}')
