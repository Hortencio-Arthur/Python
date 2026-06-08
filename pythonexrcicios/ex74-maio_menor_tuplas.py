#gerar cinco numeros aleatorios e colocar eles em uma tupla
#depois ver o maior e o menor
from random import randint

numeros = []
for n in range(5):
    numeros.append(randint(0, 10))

tupla_numeros = tuple(numeros)

#numeros_ordenados = sorted(tupla_numeros)

print(f'os seguintes numeros foram sorteados: {tupla_numeros}.')
#print(f'Dos quais o Maior é {numeros_ordenados[4]} e o Menor é {numeros_ordenados[0]}')
print(f'Dos quais o Maior é {max(tupla_numeros)} e o Menor é {min(tupla_numeros)}')


