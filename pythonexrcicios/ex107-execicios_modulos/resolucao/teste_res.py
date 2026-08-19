import moeda_res
from moeda_res import diminuir
p = float(input("Digite o preço: R$"))
print(f"A metade de R${p} é R${moeda_res.metade(p)}")
print(f"O dobro de R${p} é R${moeda_res.dobro(p)}")
print(f"Aumentado 10% de R${p}, temos R${moeda_res.aumentar(p, 10)}")
print(f"Diminuindo 10% de R${p}, temos R${diminuir(p, 10)}")