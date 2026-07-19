def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif  idade < 18 or idade > 65:
        return f'Com {idade} anos: OPICIONAL.'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO.'

#programa principla
nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))
