#fazer uma funçao chamada escreva()
# que recebe um texto qualquer de parametro e mostra uma mensagem com tamanho adaptavel

def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('~' * tamanho)

escreva('Arthur Hortencio')
escreva('pneumoultramicroscopicossilicovulcanoconiótico')
escreva('Paciência')
escreva(123)