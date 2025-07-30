opcao = 4
n1 = n2 = 0

while opcao != 5:
    n1 = int(input('Insira o 1º número: '))
    n2 = int(input('Insira o 2º número: '))
    print('-' * 40)
    print('ESCOLHA O QUE QUER FAZER:')
    print('[1] SOMAR | [2] MULTIPLICAR | [3] MAIOR NÚMERO | [4] NOVOS NÚMEROS | [5] SAIR DO PROGRAMA')
    opcao = int(input('Escolha a opção: '))
    print('-' * 40)
    if opcao == 5:
        print('Saindo...')
    elif opcao != 4:
        if opcao == 1:
            soma = n1 + n2
            print(f'A soma entre {n1} e {n2} é igual a {soma}')
            print('-' * 40)
        if opcao == 2:
            multiplicacao = n1 * n2
            print(f'O produto entre {n1} e {n2} é igual a {multiplicacao}')
            print('-' * 40)
        if opcao == 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
                print('-' * 40)
            elif n2 > n1:
                print(f'{n2} é maior que {n1}')
                print('-' * 40)
            else:
                print(f'{n1} é igual a {n2}')
                print('-' * 40)
        if opcao < 0 or opcao > 5:
            print(f'OPÇÃO INVÁLIDA!')
            print('-' * 40)

        print('ESCOLHA O QUE QUER FAZER:')
        print('[4] NOVOS NÚMEROS | [5] SAIR DO PROGRAMA')
        opcao = int(input('Escolha a opção: '))
        print('-' * 40)

print('FIM DO PROGRAMA')
