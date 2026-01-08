print('{:=^30'.format (' Lojinha do Hortencio '))
preco = float(input('Valor da compra:R$ '))
print('Formas de pagamento:'
      '[1] à vista dinheiro/cheque'
      '[2] à vista cartão'
      '[3] 2x no cartão'
      '[4] 3x ou mais no cartão')
forma = int(input('Qual a forma de pagamento? '))

if forma == 1:
    final = preco -(preco * 10 / 100)
elif forma == 2:
    final = preco - (preco * 5 / 100)
elif forma == 3:
    final = preco
    print(f'Sua compra sera parcelada em 2x de R${preco / 2 :.2f} SEM JUROS.')
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    final = preco + (preco * 20 / 100)
    vpar = final / parcelas
    print(f'Sua compra sera parcelada em {parcelas}x de R${vpar :.2f} COM JUROS. ')
else:
    final = preco
    print('Forma de pagamento invalida. tente novamente')

print(f'Sua compra de R${preco :.2f} vai custar R${final :.2f} no final.')