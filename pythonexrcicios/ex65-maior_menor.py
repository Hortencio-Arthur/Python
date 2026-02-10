'''soma = 0
cont = 0
maior = 0
menor = 0
continuar = True

while continuar:
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    sn = ''
    while sn not in 'SN':
        sn = input('Quer continuar?[S/N]:').strip().upper()[0]
    if sn == 'N':
        break

media = soma / cont
print(f'Voce digitou {cont} numeros e a media dos valores foi {media:.2f}.')
print(f'O MENOR valor foi {menor} e o MAIOR foi {maior}')'''

resp = 'S'
soma = quant = menor = maior = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0:1]
        if resp not in 'SN':
            print('Valor inválido! Por favor, digite apenas S ou N.')
media = soma / quant

print(f'Voce digitou {quant} numeros e a media foi {media}.')
print(f'o menor valor foi {menor} e o maior foi {maior}.')