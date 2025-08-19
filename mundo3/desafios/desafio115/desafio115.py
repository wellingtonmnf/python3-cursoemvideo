import menu, dados

while True:
    menu.menu()
    try:
        opcao = int(input('\033[33mSua Opção:'))
        print('\033[m')
        if opcao == 1:
            dados.ler_cadastro()
        elif opcao == 2:
            dados.cadastrar()
        elif opcao == 3:
            menu.sair()
            break
        else:
            print('\033[31mERRO! Digite uma opção válida\033[33m')
    except:
        print('\033[31mERRO! Digite um número inteiro válido\033[33m')
