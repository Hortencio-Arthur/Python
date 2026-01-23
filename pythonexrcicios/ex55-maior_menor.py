menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso :
           maior = peso
        if menor > peso:
            menor = peso

print(f'O maior peso lido é {maior}Kg')
print(f'o menor peso lido é {menor}Kg')
