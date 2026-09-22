#
# def leiadinheiro (msg):
#      flag = False
#      while not flag:
#          valor = str(input(msg)).replace(',', '.').strip()
#          if valor.isalpha() or valor == '':
#              print(f'ERRO: "{valor}" é um preço invalido! ')
#          else:
#             return float(valor)

def leiadinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'ERRO: "{valor}" é um preço invalido!')
        else:
            return float(valor)
