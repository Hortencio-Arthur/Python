#fazer um sistema de cadastro de jogadores,ex 93, dentro de um while
# depois colocar em uma lista do time
# mostrar o time em uma tabela formatada, com codigo, nome, gols, total
#conseguir levantar os dados do jogador pelo codigo, retorna a quantidade de gols em cada jogo, 999 flag
time = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))

    jogos = int(input(f'quantos jogos {jogador["nome"]} jogou?: '))
    lista_gols = []
    for c in range(jogos):
        lista_gols.append(int(input(f'Quantos gols marcou na partida {c + 1}?: ')))
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)

    time.append(jogador.copy())

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
    print('-' * 30)
print('=-' * 30)

print(f'{"Cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<5}')
print('--' * 30)
for i, jogador in enumerate(time):
    print(f'{i + 1:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<15}{jogador["total"]:<7}')
print('--' * 30)

while True:
    dados = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if dados == 999:
        print('FINALIZANDO...')
        break
    if 0 < dados <= len(time):
        dados -= 1
        print(f'-- LEVANTAMENTO DO JOGADOR [{time[dados]["nome"]}]: ')
        for i in range(len(time[dados]['gols'])):
            print(f'    No jogo {i + 1} marcou {time[dados]["gols"][i]} gols.')
    else:
        print(f'-ERRO! Nao existe jogador com codigo {dados}.')
