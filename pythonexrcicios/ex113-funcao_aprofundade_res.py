def leiaint(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print("\033[31mDigite um numero inteiro válido.\033[m")
            continue

        except KeyboardInterrupt:
            print("\n\033[31mUsuário optou por nao digitar o valor\033[m")
            return 0

        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print("\033[31mDigite um número real válido.\033[m")
            continue

        except KeyboardInterrupt:
            print("\n\033[31mDigite um número real válido.\033[m")
            return 0
        else:
            return n

#programa
n1 = leiaint("Digite um Inteiro: ")
n2 = leiafloat("Digite um Real: ")
print(f"O número inteiro digitado foi {n1} e o real foi {n2}.")