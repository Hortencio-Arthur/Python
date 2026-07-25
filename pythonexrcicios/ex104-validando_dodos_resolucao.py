def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mErro. Digite um número inteiro válido.\033[m')
    return valor

#programa principal
numero = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o número {numero}.')