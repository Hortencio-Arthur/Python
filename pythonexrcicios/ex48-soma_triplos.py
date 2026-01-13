s = 0
c = 0
for n in range(3,501,3):
    if n % 2 != 0:
        s += n
        c += 1

print(f'A soma dos {c} multiplos de 3 ate 500 é: {s}')