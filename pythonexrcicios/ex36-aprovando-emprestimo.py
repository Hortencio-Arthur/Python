'''valor = float(input('Digite o valor do imovel:R$'))
salario = float(input('Digite o seu salario:R$'))
anos= int(input('Digite em quantos anos pretende pagar:'))
prest = valor / (anos * 12)

if prest > salario / 0.3:
    resultado = str('NEGADO')

else:
    resultado = str('APROVADO')

print(f'Para pagar uma casa de valor R${valor}, com salario de {salario} em {anos} anos a prestaçao sera de R${prest} '
      f'O emprestimo foi {resultado}')'''

casa =float(input('valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de finaciamento?'))
prest =casa / (anos * 12)
minimo = salario * 0.30

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end=' ')
print(f'a prestaço sera de R${prest:.2f}')
print(f'Companranod tem  que pagar R${prest:.2f} e o minimo é de R$ {minimo:.2f}')

if prest <= minimo:
    print('Emprestimo pode ser CONCEDIDO!'
          '')
else:
    print('Emprestimo NEGADO!')

