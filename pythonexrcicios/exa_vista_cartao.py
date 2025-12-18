preco = float(input('Digite o preço do produto: R$'))
desconto = float(input("Digite o valor do desconto:%"))
juros = float(input('Digite o valor do juros do cartao:%'))
cartao = preco + (preco *  juros / 100)
vista = preco - ( preco * desconto/ 100)

print('Esse produto que custava {:.2f}, no cartao custara R${:.2f} e à vista custara R${:.2f}'.format(preco, cartao, vista))

