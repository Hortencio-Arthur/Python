#criar uma tupla com os 20 colocados do campeonato de br de futebol
#mostrar os 5 primeiros, os 4 ultimos, ordem alfabetica, Chapecoense

times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino',
         'Bahia', 'Coritiba', 'Sao Paulo', 'Atletico-MG', 'Corinthians', 'Cruzeiro',
         'Botafogo', 'EC Vitoria', 'Internacional', 'Santos', 'Gremio', 'Vasco da Gama',
         'Remo', 'Mirasol', 'Chapecoense')
chapecoense = times.index('Chapecoense') + 1
print('==' * 30)
print(f'Os cinco primeiros da serie A do Brasilheirao: {times[0:5]}')
print('==' * 30)
print(f'Os quatro ultimos do Brasilheirao serie A: {times[-4:]}')
print('==' * 30)
print(f'Os times ordernados em ordem alfabetica: {sorted(times)}')
print('==' * 30)
print(f'Posiçao do Chapecoense: °{chapecoense} colocado')

