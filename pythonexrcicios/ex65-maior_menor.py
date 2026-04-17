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

soma = quant = menor = maior = 0
while True:
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
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0:1]
        if resp in 'SN':
            break
        print('Valor inválido! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break

media = soma / quant

print(f'Voce digitou {quant} numeros e a media foi {media:.f2}.')
print(f'o menor valor foi {menor} e o maior foi {maior}.')