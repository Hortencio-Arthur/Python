#criar função ficha(), com os dois parâmetros opcionais:
# - nome do jogador
# - gols do jogador
# mostrar a ficha mesmo que os dados nao tenham sido informados corretamente
nome_teste = "Arthur"
def ficha(nome='<desconhecido>', gols=0):
    print(f'O Jogador [{nome}] fez [{gols}] gol(s) no campeonato.')


#principal
nome_jogador = str(input('Nome do jogador: '))
gols_jogador = str(input('Número de gols: '))
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)