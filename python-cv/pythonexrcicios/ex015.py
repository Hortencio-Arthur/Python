dias = int(input('Digite quantos dias o carro foi alugado: '))
Km = float(input('Digite quantos km foram rodados:'))
valor = (dias * 60) + (Km * 0.15)
print('O valor a pagar por {} dias e {}Km é R${:.2f}'.format(dias, Km, valor))
