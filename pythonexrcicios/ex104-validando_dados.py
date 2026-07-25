#criar uma função chamada leiaint()
#ele vai funcionar como um input com validação para aceitar apenas numericos

def leiaint(valor):

    while True:
        num = input(valor)
        if num.isnumeric():
            intnum = int(num)
            break
        else:
            print('\033[31mErro. Digite um numero inteiro valido.\033[m')

    return intnum
#principal
n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}.')