dist = float(input('Digite a distancia da viagem em Km/h:'))

'''if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45'''
preco = dist * 0.50 if dist <= 200 else dist * 0.45# forma simplificada

print('O valor da sua passagem foi de R${:.2f}'.format(preco))