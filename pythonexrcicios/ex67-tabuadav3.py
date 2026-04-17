"""
- fazer uma tabuada que mostra a tabuada de diversos numeros, um por vez sem
interromper o programa
- usa um numero negativo como flag

"""
print('TABUADA V3')
while True:
    try:
        n = int(input('Digite um numero:'))
        print('==' * 10)
    except ValueError:
        print('Valor invalido tente novamente!')
        continue
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} X {c:2} = {n * c:3}')
    print('==' * 10)


print('Encerrando...')