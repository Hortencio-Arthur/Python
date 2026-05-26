# ---------------------------------------------------------
# Script: calculo_fatorial.py
# Objetivo: Calcular o fatorial de um número entre 1 e 10.
# ---------------------------------------------------------

from math import factorial

# Inicializamos a variável que guardará o número validado
numero_escolhido = 0

while True:
    try:
        entrada_usuario = input('Digite um número inteiro de 1 a 10: ')

        # A linha abaixo realiza o casting (conversão explícita):
        # transformamos a string recebida do input em um número inteiro (int).
        numero_escolhido = int(entrada_usuario)

        if 1 <= numero_escolhido <= 10:
            break
        else:
            print('Por favor, digite um número dentro do intervalo (1 a 10).')
    except ValueError:
        print('Entrada inválida! Certifique-se de digitar um número inteiro.')

# Após a validação, calculamos o fatorial usando a biblioteca math
resultado_final = factorial(numero_escolhido)

print(f'O fatorial de {numero_escolhido} é: {resultado_final}')