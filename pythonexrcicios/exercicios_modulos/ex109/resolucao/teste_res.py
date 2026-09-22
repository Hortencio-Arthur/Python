import moeda_res

p = float(input("Digite o preço: R$"))
print(f"A metade de {moeda_res.moeda(p)} é {moeda_res.metade(p, True)}")
print(f"O dobro de {moeda_res.moeda(p)} é {moeda_res.dobro(p, True)}")
print(f"Aumentado 10%, temos {moeda_res.aumentar(p, 10, True)}")
print(f"Diminuindo 10%, temos {moeda_res.diminuir(p, 10, True)}")