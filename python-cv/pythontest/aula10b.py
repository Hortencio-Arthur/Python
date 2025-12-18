n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

print('Sua media foi {}'.format(media))
print('Parabens' if media >= 6 else'estude mais')