#fazer uma funçao chamada contador()
#que vai receber tres parâmetros:inicio, fim e passo
# com a funçao fazer tres contagens:
#  a-1 ate 10, de 1 em 1
#  b-10 ate 0, 2 em 2
#  c-personalizada
from time import sleep
def contador(inicio, fim, passo):
    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')

    if inicio > fim:
        fim -= 1
        if passo >= 0:
            passo = -passo
    if fim >= inicio:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.25)

    print('Fim!')

#codigo principal
#contagem A
contador(1, 10 , 1)
#contagem B
contador(10, 0, 2)
#contagem C
print('Personalize a sua contagem:')
inicio_perso = int(input('Inicio: '))
fim_perso  = int(input('Fim: '))
passo_perso = int(input('Passo: '))
contador(inicio_perso, fim_perso, passo_perso)