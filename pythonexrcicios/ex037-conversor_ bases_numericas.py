'''num = int(input('Digite qual o numero que voce quer converter?: '))
base = int(input('Digite qual base voce vai usar: '))
print('Binario[1]')
print('Octal[2]')
print('Hexadecimal[3]')
if base == 1:
    print(bin(num))

elif base == 2:
    print(oct(num))
elif base == 3:
    print(hex(num))
'''
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao
[1]converter para BINARIO
[2]converter para OCTAL
[3]converter para HEXADECIMAL''')
opçao = int(input('Sua opçao:'))

if opçao == 1:
    print(f'O numero {num} em binario é {bin(num)[2:]} ')
elif opçao == 2:
    print(f'O numero {num} em octal é {oct(num)[2:]} ')
elif opçao == 3:
    print(f'O numero {num} em hexadecimal é {hex(num)[2:]} ')
else:
    print('opçao invalida tente novamente')