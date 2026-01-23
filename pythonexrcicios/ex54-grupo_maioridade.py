from datetime import date
ano = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    nasc = int(input(f'Data de nascimento da {c}° pessoa: '))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também {menor} menores de idade')
