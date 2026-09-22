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
