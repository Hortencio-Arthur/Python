print('---Radar de velocidade---')
velo = float(input('Digite a velocidade em Km/h:'))
multa = (velo - 80) * 7

if velo > 80:
    print('MULTADO! Acima do limite de velocidade. A multa foi de R${:.2f}. '.format(multa))
else:
    print('Esta dentro do limite de velociade =)')

print('Tenha um bom dia! Dirija com segurança')