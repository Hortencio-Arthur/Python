salario = float(input('Qual o salario do funcionario?:R$ '))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)

print('O salario foi de R${:.2f} para R${:.2f}'.format(salario, aumento ))