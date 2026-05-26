"""
- ler o nome e o preço de varios produtos X
- perguntar se o usuario quer continuar X
- ao final mostrar
    -gasto total X
    - produtos que custam mais de 1000 reais X
    - nome do produto mais barato X
"""
cont = totmil = menor = soma = 0
barato = ' '
while True:
    cont += 1
    print('==' * 10)
    print(f'#Cadastro N{cont}')
    nome = str(input('Nome do produto: '))
    try:
        preco = float(input('Preço do produto:R$'))
    except ValueError:
        print('Valor invalido! tente novamente.')
        cont -= 1
        continue

    soma += preco
    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 10)
print(f'O gasto total foi de R${soma:.2f}')
print(f'{totmil} produtos passam dos R$1000!')
print(f'O produto com menor preço foi {barato} que custa {menor}')
print('Encerrando...')