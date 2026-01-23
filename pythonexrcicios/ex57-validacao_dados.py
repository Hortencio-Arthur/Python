sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0]

while sexo not in 'MF':
    print('Dados invalidos!', end=' ')
    sexo = str(input('Por favor, informe o seu sexo: ')).upper().strip()[0]

print(f'Sexo {sexo} Registrado!')