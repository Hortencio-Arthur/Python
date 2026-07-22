#fazer funcao fatorial() com dois parametros:
# - numero a calcular, numero a ser feito o fatorial
# - show, valor logico opcional, indica se sera mostrado ou nao
# o processo do calculo fatorial na tela
def fatorial(num, show=False):
    """
    -Calcula o fatorial de um número.
    :param num: Número a ser calculado
    :param show: (opcional) Mostra ou nao o processo de calculo.
    :return: Valor do fatorial de número n.
    """
    fator = 1
    for c in range(num, 0, -1):
        fator *= c
        if show:
            print(f'{c}{" x" if c > 1 else ""}', end=' ')
    if show:
        print('=', end= ' ')
    return fator

#programa principal
print(fatorial(5, show=False))
help(fatorial)