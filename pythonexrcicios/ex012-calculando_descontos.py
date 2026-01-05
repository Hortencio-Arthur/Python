'''p = float(input('Digite o preço do produto: '))
d = p-(p*(5/100))

print('esse produto fica com o valor de R${} com 5% de desconto'.format(d))'''

preco = float(input('Qual é o preço do produto? R$'))
novo = preco-(preco * 5/ 100)

print('o produto que custava R${:.2f} com desconto de 5% custa R${:.2f}'.format(preco, novo))