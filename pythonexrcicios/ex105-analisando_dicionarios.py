#criar def notas(), recebe varias notas,arg*,
#retorna a maior nota, a menor nota, media das notas, situacao opcional

def notas(*nota, sit=False):
    """
    -Fução para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunoa (aceita várias)
    :param sit: valor opcional, indicando ou nao mostrar a situação da turma
    :return:dicionário com varias informações sobre a situação da turma.
    """
    anotacao = dict()
    anotacao['total'] = len(nota)

    maior = menor = soma = 0
    for i, n in enumerate(nota):
        if i == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

        soma += n
    anotacao['maior'] = maior
    anotacao['menor'] = menor
    anotacao['media'] = soma / anotacao['total']

    if sit:
        if anotacao['media'] >= 7:
            situacao = 'BOA'
        elif anotacao['media'] >= 5:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        anotacao['situacao'] = situacao

    return anotacao
#programa principal
resposta = notas(10,9 ,3, sit=True)
print(resposta)
help(notas)