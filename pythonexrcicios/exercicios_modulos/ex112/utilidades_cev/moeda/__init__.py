def dobro(preco, formato=False):
    res =  preco * 2
    return res if not formato else moeda(res)

def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def aumentar(preco, taxa, formato=False):
    res = preco + ( preco * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preco, taxa, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)

def moeda(preco):
    res = f'R${preco:.2f}'
    return res

def resumo(preco=0, aumento=10, reducao=10, forma=False):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)

    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, forma)}')
    print(f'Dobro do preço: \t{dobro(preco, forma)}')
    print(f'Aumento de {aumento}%: \t{aumentar(preco, aumento, forma)}')
    print(f'Redução de {reducao}%: \t{diminuir(preco, reducao, forma)}')

    print('-' * 40)