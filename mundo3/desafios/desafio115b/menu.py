from mundo3.desafios.desafio115b import dados


def linha(tamanho=50):
    print('-' * tamanho)


def titulo(txt):
    linha()
    print(txt.center(50))
    linha()


def item(num=0, txt='item'):
    return f'\033[1:33m{num} -\033[m \033[1:34m{txt}\033[m'


def menu():
    titulo('MENU PRINCIPAL')
    print(item(1, 'Ver pessoas cadastradas'))
    print(item(2, 'Cadastrar nova pessoa'))
    print(item(3, 'Sair do sistema'))
    linha()


def ler_opcao(num=0):
    print('\033[33m')
    opcao = dados.leiaInt('Sua Opção: ')
    print('\033[m')
    return opcao


def mostrar_erro(txt='Tente novamente'):
    return f'\033[1:31mERRO! {txt}\033[m'


def mostrar_sucesso(txt='Processo finalizado'):
    return f'\033[1:32m{txt}\033[m'
