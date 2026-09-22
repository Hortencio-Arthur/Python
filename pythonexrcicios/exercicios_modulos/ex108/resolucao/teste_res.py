import moeda_res

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda_res.moeda(p)} é {moeda_res.moeda(moeda_res.metade(p))}")
print(f"O dobro de {moeda_res.moeda(p)} é {moeda_res.moeda(moeda_res.dobro(p))}")
print(f"Aumentado 10%, temos {moeda_res.moeda(moeda_res.aumentar(p, 10))}")
print(f"Diminuindo 10%, temos {moeda_res.moeda(moeda_res.diminuir(p, 10))}")