#perguntar qual valor a ser sacado, numero inteiro
#o program vai informar quantas cedulas de cada valor vao ser entregues
#caixa tem notas de 50, 20, 10 e 1
print('=' * 30)
print('{:^30}'.format('BANCO HORTENCIO'))
print('=' * 30)

saque_dinheiro = valor_total = 0
while True:
    entrada_dinheiro = input('Digite o valor do saque: R$').strip()
    try:
        saque_dinheiro = int(entrada_dinheiro)
        if saque_dinheiro <= 0:
            print('Valor  inválido. Digite um valor maior que 0')
            continue
        valor_total = saque_dinheiro
        break
    except ValueError:
        print('Valor inválido. Digite um numero inteiro.')
        continue
total_cedula = 0
cedula_atual = 50
while True:
    if valor_total >= cedula_atual:
        valor_total -= cedula_atual
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} de R${cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedula = 0
        if valor_total == 0:
            break

print('=' * 30)
print('Volte Sempre!')
