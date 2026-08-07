#criar um mini-sistema de ajuda, usando o help()
#usuario vai digitar o comando e o manual vai aparecer
#digitando FIM, acaba o programa
#usar cores
def titulo():
    print('\033[;43m', end='')
    print('~' * 30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~' * 30)
    print('\033[m')
def comando(texto):
    tamanho = len(texto) + 40
    print('\033[7;34m', end='')
    print('~' * tamanho)
    print(f'{f"Acessando o manual do comando[{texto}].":^{tamanho}}')
    print('~' * tamanho)
    print('\033[m')
def manual(funcao):
    print('\033[97;7m', end='')
    help(funcao)
    print('\033[m')
#programa principal
while True:
    titulo()
    fonte = str(input('Função ou Biblioteca> ')).strip().lower()
    if fonte == 'fim':
        break
    comando(fonte)
    manual(fonte)
print('\033[41m~' * 15)
print('ATÉ LOGO')
print('~' * 15)
print('\033[m')