#script: Calculo Fatorial
#calculo fatorial  de um numero inteiro positivo que seja de 1 a 10

from math import factorial
numero = 0
while True:
    try:
        numero = int(input('Digite um número de 1 a 10: '))
        if  0 < numero <= 10:
            break
        else:
            print('Por favor, Digite um número de 1 a 10.')
            continue
    except ValueError:
        print('Valor inválido. Por favor, digite um número.')
        continue
resultado_fatorial = factorial(numero)

print(f'O resultado de {numero}! é {resultado_fatorial}.')