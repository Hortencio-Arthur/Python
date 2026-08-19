import moeda
from moeda import metade, diminuir
valor = float(input("Digite o Preço: "))
print(f"A metade de R${valor} é R${metade(valor)} ")
print(f"O dobro de R${valor} é R${moeda.dobro(2)}")
input_aumento = float(input("Digite o valor do aumento:% "))
print(f"O preço R${valor} com um aumento de {input_aumento}% é R${moeda.aumentar(valor, input_aumento)} ")
input_reducao = float(input("Digite o valor do desconto:% "))
print(f"O valor R${valor} com o desconto de {input_reducao}% é de R${diminuir(valor, input_reducao)}")