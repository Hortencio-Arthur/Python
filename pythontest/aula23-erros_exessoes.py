try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos problemas com o tipo de dados que você informou.')

except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero.')

except KeyboardInterrupt:
    print('Usuario preferiu por não optar os dados.')

except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')

else:
    print(f'O resultado foi {r:.1f}')

finally:
    print('Volte sempre!')
