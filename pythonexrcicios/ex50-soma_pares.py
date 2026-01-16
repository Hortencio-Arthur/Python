s = 0
con = 0
for c in range (1,7):
    n = int(input(f'{c}° numero: '))
    if n % 2 == 0:
        s += n
        con +=1

print(f'A soma dos {con} numeros pares é {s}')