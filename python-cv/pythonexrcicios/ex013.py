"""s = float(input('Digite o salario: '))
a = s+(s*(15/100))

print('O salario com o aumento fica {}R$'.format(a))"""

salario = float(input('Digite o salario do funcionario:R$'))
novo = salario + (salario * 15 / 100)

print('um funcionario que ganhava R${:.2f} com o aumento ganha R${:.2f}'.format(salario, novo))
