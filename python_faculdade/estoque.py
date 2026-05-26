# Escolha técnica: Dicionário de Dicionários
# Justificativa: Foi escolhida essa opção devido ao acesso mais rápido aos produtos
# e pela escalabilidade para o programa.

from time import sleep

print('== Gestão de Estoque ==')

# Inicialização do banco de dados (estoque)
produto_estoque = {
    'MOUSE': {'quantidade': 10, 'preco': 50.00},
    'TECLADO': {'quantidade': 7, 'preco': 200.00},
    'MONITOR': {'quantidade': 5, 'preco': 550.00}
}

while True:
    print('==' * 15)
    print('-- Escolha uma Opção abaixo:')
    print('==' * 15)
    print('   1-Visualizar Estoque Atual')
    print('   2-Registrar Entrada de Produto')
    print('   3-Registrar Saída de Produto')
    print('   4-Sair do Sistema')
    print('==' * 20)

    opcao_str = input('Digite sua opção: ').strip()

    # Opção de Encerramento 
    if opcao_str == '4':
        print('=' * 30)
        print('# Finalizando programa... Operações realizadas com sucesso!')
        break

    # Opção 1: Visualização do Estoque
    elif opcao_str == '1':
        print('=' * 30)
        print(f'{"PRODUTO":<10} | {"QTD":<10} | {"PREÇO":<10}')
        print('-' * 40)
        for produto_nome, dados_produto in produto_estoque.items():
            print(f'{produto_nome:<10} | {dados_produto["quantidade"]:<10} | '
                  f'{dados_produto["preco"]:<10.2f}')
        sleep(2)

    # Opção 2: Entrada de Estoque
    elif opcao_str == '2':
        while True:
            nome_digitado = input('Digite o nome do produto: ').strip().upper()

            if nome_digitado in produto_estoque:
                try:
                    quantidade_entrada = int(input('Digite a quantidade: '))

                    # Validação para garantir entrada de valores positivos
                    if quantidade_entrada > 0:
                        produto_estoque[nome_digitado]["quantidade"] += quantidade_entrada
                        print('Estoque atualizado!')
                        print(f'Estoque atual de {nome_digitado} é de: '
                              f'{produto_estoque[nome_digitado]["quantidade"]}')
                        break
                    else:
                        print('Valor inválido. Digite um número positivo.')
                except ValueError:
                    print('Valor inválido. Digite um número inteiro.')
            else:
                print('Produto não encontrado. Tente novamente.')
                continue
        sleep(2)

    # Opção 3: Saída de Estoque
    elif opcao_str == '3':
        while True:
            nome_digitado = input('Digite o nome do produto: ').strip().upper()

            # Valida se o produto existe antes de solicitar a quantidade
            if nome_digitado in produto_estoque:
                try:
                    quantidade_saida = int(input('Digite a quantidade: '))

                    if quantidade_saida > 0:
                        estoque_atual = produto_estoque[nome_digitado]["quantidade"]

                        # Regra de Negócio: Impede que o estoque fique negativo
                        if estoque_atual < quantidade_saida:
                            print(f'Estoque insuficiente. Estoque atual: {estoque_atual}')
                            continue
                        else:
                            produto_estoque[nome_digitado]["quantidade"] -= quantidade_saida
                            print('Estoque atualizado!')
                            print(f'Estoque atual de {nome_digitado} é de: '
                                  f'{produto_estoque[nome_digitado]["quantidade"]}')
                            break
                    else:
                        print('Valor inválido. Digite um número positivo.')
                except ValueError:
                    print('Valor inválido. Digite um número inteiro.')
            else:
                print('Produto não encontrado. Tente novamente.')
                continue
        sleep(2)

    # Bloco Else: Fallback para opções inválidas no menu principal
    else:
        print(f'A opção {opcao_str} é inválida. Escolha entre 1 e 4.')