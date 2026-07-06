#Criar uma funçao chamada area(), que receba largura e comprimento
#que calcule a area de um retangulo, largura*comprimento
# e mostre a area no final

def area(largura, comprimento):
    print(f'A area de um terreno de {largura:.1f}m x {comprimento:.1f}m é de {largura * comprimento:.1f}m².')

print(f'{"Controle de terrenos":^30}')
print('=' * 30)

largura_terreno = float(input('Largura(m): '))
comprimento_terreno = float(input('Comprimento(m): '))

area(largura_terreno,comprimento_terreno)