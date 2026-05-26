def calcular_media(notas):
    """
    Calcula a média aritmética simples de uma lista de notas.

    Args:
        notas (list): Lista contendo as notas dos alunos em float.

    Returns:
        float: A média das notas calculadas.
    """
    # Proteção contra erro de divisão por zero caso o aluno não tenha notas
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Verifica se o aluno foi aprovado ou reprovado com base na comparação da média com a média mínima.

    Args:
        media (float): Média final feita com as notas do aluno.
        media_minima (float): Nota mínima para ser aprovado. O padrão é 7.0.

    Returns:
        str: 'APROVADO' ou 'REPROVADO'.
    """
    if media >= media_minima:
        return 'APROVADO'
    else:
        return 'REPROVADO'


def gerar_relatorio(alunos):
    """
    Gera o relatório completo dos alunos, com nome, notas, média e resultado do aluno.

    Args:
        alunos (list): Lista com os alunos.

    Returns:
        None
    """
    for aluno in alunos:
        # Extração dos dados do dicionário do aluno atual
        nome_aluno = aluno['nome']
        notas_aluno = aluno['notas']

        # Processamento lógico utilizando as funções especialistas
        media_aluno = calcular_media(notas_aluno)
        resultado_aluno = verificar_aprovacao(media_aluno)

        # Exibição dos dados formatados (remover recuos mantém o alinhamento no terminal)
        print('--' * 30)
        print(f'''[ALUNO: {nome_aluno}] 
[NOTAS: {notas_aluno}] 
[MÉDIA: {media_aluno:.2f}]
[RESULTADO: {resultado_aluno}]''')


# Repositório de dados em memória (Simulação de banco de dados para testes)
lista_alunos = [
    {
        "nome": "Ana Silva",
        "notas": [8.5, 7.5, 9.0]
    },
    {
        "nome": "Carlos Souza",
        "notas": [5.0, 6.0, 5.5]
    },
    {
        "nome": "Mariana Costa",
        "notas": [9.5, 10.0, 8.8]
    },
    {
        "nome": "Ricardo Oliveira",
        "notas": [3.0, 4.5, 2.0]
    },
    {
        "nome": "Juliana Lima",
        "notas": [7.0, 7.0, 7.5]
    }
]

# Bloco de execução principal do programa
print('{:^30}.'.format('Relatório Acadêmico'))
print('==' * 30)
gerar_relatorio(lista_alunos)