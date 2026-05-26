# Script: conversor_temperatura.py
# Objetivo: Converter Celsius para Fahrenheit com tratamento de erros.

print('CONVERSOR C° para F°')
print('===' * 10)

# Inicializamos as variáveis para garantir que existam no escopo global
temperatura_celsius = temperatura_fahrenheit = 0.0

while True:
    try:
        # CAPTURA E CONVERSÃO (CASTING):
        # O input() recebe dados como texto (string).
        # Usamos float() para converter explicitamente esse texto em um número decimal,
        # permitindo que cálculos matemáticos sejam realizados.
        temperatura_celsius = float(input('Digite a temperatura em graus Celsius [C°]: '))

        # Processamento: Aplicação da fórmula de conversão
        temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32

        # Se as linhas acima funcionarem sem erro, interrompemos o laço
        break

    except ValueError:
        # Tratamento de erro caso o usuário digite letras ou símbolos inválidos
        print('Erro: Valor inválido. Por favor, digite um número (ex: 25.5).')
        continue

# Saída de dados com f-strings e formatação de 2 casas decimais (:.2f)
print(f'A temperatura {temperatura_celsius:.2f}°C '
      f'em graus Fahrenheit é {temperatura_fahrenheit:.2f}°F')