#criar uma função chamada voto()
#recebe o parâmetro do ano do nascimento de uma pessoa
#retorna um valor literal/string, que indica se a pessoa tem o voto negado, opcional ou obrigatorio
from datetime import date

def voto(nasc):
    idade = date.today().year - nasc
    situacao = ''

    if 16 <= idade <= 17 or idade > 70:
        situacao = 'OPCIONAL'
    elif idade >= 18:
        situacao = 'OBRIGATÓRIO'
    else:
        situacao = 'NEGADO'

    return idade, situacao

#principal
print('_' * 30)
data_nasc = int(input('Em que ano você nasceu?: '))
idade_pessoa, situacao_voto = voto(data_nasc)
print(f'Com {idade_pessoa} anos: {situacao_voto}.')