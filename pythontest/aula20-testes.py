"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)

#programa principal
soma(b=4, a=5)
soma(2,1)
soma(8, 9)"""

""""def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')
   tam = len(num)
   print(f'Recebi os valores {num} e sao ao todo {tam} numeros.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 5, 2)"""
""""
def dobra(lista):
    for i, n in enumerate(lista):
        lista[i] *= 2


valores = [6, 3, 0, 5, 8, 4]
dobra(valores)
print(valores)
"""
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} e {s}')

soma(5,2)