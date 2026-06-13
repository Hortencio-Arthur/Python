#soluçao do curso
temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    principal.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

print('=-' * 30)
print(f'Ao todo foram cadastrados {len(principal)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='' )
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
