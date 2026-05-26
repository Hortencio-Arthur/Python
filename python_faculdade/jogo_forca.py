from random import choice


def inicializar_jogo():
    """
    Prepara o estado inicial do jogo da forca.

    Processamento: Armazena o banco de palavras em uma lista, sorteia uma
    palavra aleatoriamente e gera a máscara de tracinhos correspondente.

    Returns:
        tuple: Uma tupla contendo (palavra_secreta, lista_oculta_de_tracinhos).
    """
    palavras_forca = ['PYTHON', 'DADOS', 'LISTA', 'TUPLA',
                      'DICIONARIO', 'CONJUNTO', 'ESTRUTURA']
    sorteio_palavra = choice(palavras_forca)
    olcutar_palavra = ['_'] * len(sorteio_palavra)

    return sorteio_palavra, olcutar_palavra


def processamento_jogo(chute, palavra_secreta, lista_oculta):
    """
    Processa o palpite do jogador na rodada atual e atualiza a máscara do jogo.

    Args:
        chute (str): Letra digitada pelo jogador.
        palavra_secreta (str): A palavra que deve ser adivinhada.
        lista_oculta (list): O estado atual dos acertos (com tracinhos e letras).

    Returns:
        list: A lista oculta atualizada com as letras reveladas, se houver acerto.
    """
    if chute in palavra_secreta:
        print(f'##Acertou! A letra [{chute}] faz parte da palavra!')
        for indice, letra in enumerate(palavra_secreta):
            if letra == chute:
                lista_oculta[indice] = chute
    else:
        print(f'##Errou! A letra [{chute}] não esta na palavra.')
    return lista_oculta


# ==============================================================================
# FLUXO PRINCIPAL DO PROGRAMA (Mecanismo do Jogo)
# ==============================================================================

palavra_sorteada, palavra_oculta = inicializar_jogo()

# JUSTIFICATIVA DA ESTRUTURA DE DADOS (Critério de Avaliação):
# Optou-se pelo uso de Conjuntos (Sets) em vez de Listas para 'letras_tentadas' por dois motivos:
# 1. Otimização de busca: Verificar a existência de um item em um 'set' (chutes_jogador in letras_tentadas)
#    possui complexidade de tempo constante O(1), sendo muito mais rápido do que em uma lista O(n).
# 2. Unicidade: Conjuntos impedem elementos duplicados por padrão de forma nativa.
letras_tentadas = set()
tentativas_jogador = 6

while tentativas_jogador > 0 and '_' in palavra_oculta:
    print(f'===PALAVRA: {palavra_oculta}')
    chutes_jogador = input('Tente acertar uma letra da palavra: ').strip().upper()

    # Validação de Entrada: Protege contra strings vazias, múltiplos caracteres ou símbolos/números
    if not chutes_jogador or len(chutes_jogador) > 1 or not chutes_jogador.isalpha():
        print('[ERRO] entrada inválida. Digite apenas UMA letra (A-Z), Sem números ou símbolso')
        continue

    # Validação de Letra Repetida: Checa no Set se a letra já foi usada antes de processar
    if chutes_jogador in letras_tentadas:
        print('##Essa letra ja foi digitada!')
        continue

    # Adiciona a nova letra ao conjunto de tentativas após validar que ela é inédita
    letras_tentadas.add(chutes_jogador)

    # Controle de Penalidade: Reduz as tentativas apenas se o palpite inédito estiver incorreto
    if chutes_jogador not in palavra_sorteada:
        tentativas_jogador -= 1

    # Atualiza o estado das letras descobertas na palavra oculta
    processamento_jogo(chutes_jogador, palavra_sorteada, palavra_oculta)

    # Exibição do feedback de status ao término da rodada válida
    print(f'Tentativas: {tentativas_jogador}')
    print(f'Letras tentadas: {letras_tentadas}')
    print('= =' * 20)

# Verificação das condições de encerramento do jogo
if tentativas_jogador == 0:
    print(f'Não foi dessa vez! a palavra era: {palavra_sorteada}')
else:
    print(f'Parabens! você acertou a palavra {palavra_sorteada} '
          f'com {tentativas_jogador}!')