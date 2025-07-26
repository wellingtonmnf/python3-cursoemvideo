print('=' * 30)
print(f'{"TESTADOR DE NÚMEROS PRIMOS":^30}')
print('=' * 30)

n = int(input('Digite um número inteiro (>0): '))
cont = 0
divisores = ''
print('=' * 30)

if n <= 0:
    print(f'OPÇÃO INVÁLIDA!\nInforme um número inteiro \033[33mMAIOR que 0\033[m')
else:
    for c in range(1, n + 1):
        if n % c == 0:
            cont += 1
            divisores += f'\033[32m{c}\033[m '
        else:
            divisores += f'\033[31m{c}\033[m '
    print(f'O número {n} foi divisível {cont} vezes')
    print(f'Divisores: {divisores}')
    if cont != 2:
        print(f'E por isso ele \033[31mNÃO É PRIMO\033[m')
    else:
        print(f'E por isso ele \033[32mÉ PRIMO\033[m')
