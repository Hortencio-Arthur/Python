#pegar varios valores pelo teclado
#colocar eles em uma lista
#nao adicionar valores repetidos
#ao final mostrar so os unicos e em ordem crescente

valores = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Nao sera adicionado...')

    res = ' '
    while res not in 'SN':
        res = input('Quer continuar?[S/N]: ').strip().upper()[0]
    if res == 'N':
        break

print(f'aqui estao os valores unicos: {sorted(valores)}')
