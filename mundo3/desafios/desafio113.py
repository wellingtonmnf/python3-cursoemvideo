def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except Exception:
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except Exception:
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return num


print('-' * 30)
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
