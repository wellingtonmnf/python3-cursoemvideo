import menu, dados

arquivo = 'dados/cadastro.txt'

if not dados.arquivo_existe(arquivo):
    dados.criar_arquivo(arquivo)

while True:
    menu.menu()
    try:
        opcao = menu.ler_opcao()
        if opcao == 1:
            dados.ler_cadastro(arquivo)
        elif opcao == 2:
            dados.cadastrar(arquivo)
        elif opcao == 3:
            menu.titulo('Saindo do sistema... Até logo!')
            break
        else:
            print(menu.mostrar_erro('Digite uma opção válida'))
    except:
        print(menu.mostrar_erro('Digite um número inteiro válido'))
