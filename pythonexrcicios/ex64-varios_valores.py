'''print('Digite 999 para parar')
chave = False
soma = 0
cont = 0
while not chave :
    n = int(input('Digite um valor:'))
    if n != 999:
        soma += n
        cont += 1
    else:
        chave = True

print('Fim')
print(f'forma {cont} e a soma deles foi {soma}')'''

cont = soma = 0
n = int(input('Digite um numero [999 para parar]:'))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero[999 para parar]'))
print(f'Foram digitados {cont} numeros e a soma entre eles foi de {soma}')