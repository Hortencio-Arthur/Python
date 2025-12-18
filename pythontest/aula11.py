print('\033[1;30;41mTeste de cores\033[m')
print('\033[7;30mOla, mundo!\033[m')
print('\033[7;33;44mInverter cores\033[m')

a = 4
b = 5

print('Os valores são \033[31;46m{}\033[m e \033[33;40m{}\033[m'.format(a,b))

nome = 'Arthur'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto': '\033[7;30m',
         'vermelho': '\033[31m'}
print('Olá, muito prazer {}{}{}'.format(cores['vermelho'], nome, cores['limpa']))

