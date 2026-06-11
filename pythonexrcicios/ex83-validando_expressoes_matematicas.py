#usuariio digitar uma experessao matematica qualquer com parenteses
#verificar se os parenteses estao abertos e fechados na ordem correta
#esse codigo nao esta correto, pois a soluçao necessita de uma pilha
#conteudo que eu ainda nao sei utilizar na pratica, entao segui o video da soluçao para esse exercicio
""""expr = str(input('Digite uma expressao matematica: '))
lista_expr = list(expr)
lista_aberto = []
lista_fechado = []

for elemento in lista_expr:
   if elemento == '(':
       lista_aberto.append('(')
   if elemento == ')':
        lista_fechado.append(')')

if len(lista_aberto) == len(lista_fechado):
    print('verificada')
else:
    print('incorreta')"""

#codigo do curso
expr = str(input('Digire uma expressão matematica: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('A sua expressão esta errada!')

