#criar uma tupla com palavras, sem acento
#mostrar as vogais nas palavras

palavras = ('Python', 'Excalibur', 'Filhote', 'Transformacao',
            'Eu', 'jogos', 'animacao', 'Autentico', 'Dados',)

for palavra in palavras:
    print(f'Palavra:{palavra}')
    palavra = palavra.upper()
    print('Vogais:', end = ' ')

    letras = []
    for letra in palavra:
            if letra.upper() in 'AEIOU' and letra not in letras:
                letras.append(letra)

    for letra in letras:
        print(letra, end = ' ')
    print()

    print('-' * 40)