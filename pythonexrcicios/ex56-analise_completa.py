sidade =0
maioridadeh = 1
nomevelho = ''
contmulher = 0
for p in range(1, 5):
    print(f'----- Pessoa n°{p} ------')
    nome = str(input(f'Nome : ')).strip()
    idade = int(input(f'Idade : '))
    sexo = str(input(f'sexo [M/F]: ')).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
media = sidade / 4
print(f'A media das idade é {media}')
print(f'O nome do homem mais velho é {nomevelho} e ele tem {maioridadeh} anos')
print(f'Tem {contmulher} mulheres com menos de 20 anos')