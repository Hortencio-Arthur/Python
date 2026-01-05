vn1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'Com as notas {n1} e {n2}, a media do aluno foi {media:.1f}')
if media >= 7:
    print('APROVADO!')
elif 5 <= media < 6.9:
    print('RECUPERAÇAO')
elif media < 5:
    print('REPROVADO')
