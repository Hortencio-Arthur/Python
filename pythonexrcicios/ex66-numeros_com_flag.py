s = cont =  0
while True:
    n = int(input(' Digite um numero inteiro ou 999 para parar: '))
    if n == 999:
        break
    cont += 1
    s += n

print(f'Foram digitados {cont} numeros e a soma deles é {s}.')