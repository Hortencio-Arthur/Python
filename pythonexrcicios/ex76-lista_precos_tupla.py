estoque = ('Lapis', 1.75,
           'Borracha', 2,
           'Laderno', 15.9,
           'Estojo', 25,
           'Transferidor', 4.2,
           'Compasso', 9.99,
           'Mochila', 120.32 ,
           'Canetas', 22.3,
           'livro', 34.9)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS" :^40}')
print('-' * 40)

for pos in range(0, len(estoque), 2):
    item = estoque[pos]
    preco = estoque[pos + 1]
    print(f'{item:.<30}R$ {preco:>7.2f}')

print('-' * 40)