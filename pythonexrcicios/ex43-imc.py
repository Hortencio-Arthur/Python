peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Com o peso de {peso} e a altura de {altura} o seu IMC é de {round(imc, 1)}')

if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <=25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MORBIDA')