"""
- ler o nome e o preço de varios produtos
- perguntar se o usuario quer continuar
- ao final mostrar
    -gasto total
    - produtos que custam mais de 1000 reais
    - nome do produto mais barato
"""
cont = soma = 0
while True:
    cont += 1
    print(f'#Cadastro N{cont}')
    nome = str(input('Qual o nome do produto?: '))
    try:
        preco = float(input('Qual é o preço do produto?:'))
    except ValueError:
        print('Valor invalido! tente novamente.')
        cont -= 1
        continue
    soma += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O gasto total foi de R${soma:.2f}')
print('Encerrando...')