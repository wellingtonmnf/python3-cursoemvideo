print('=' * 30)
print(f'{"TESTADOR DE NÚMEROS PRIMOS":^30}')
print('=' * 30)

n = int(input('Digite um número inteiro (>0): '))
cont = 0
print('=' * 30)

if n <= 0:
    print(f'OPÇÃO INVÁLIDA!\nInforme um número inteiro \033[33mMAIOR que 0\033[m')
else:
    print(f'Divisores: ', end='')
    for c in range(1, n + 1):
        if n % c == 0:
            cont += 1
            print(f'\033[32m', end='')
        else:
            print(f'\033[31m', end='')
        print(c, end=' ')

    print(f'\n\033[mO número {n} foi divisível {cont} vezes')
    if cont == 2:
        print(f'E por isso ele É PRIMO')
    else:
        print(f'E por isso ele NÃO É PRIMO')
