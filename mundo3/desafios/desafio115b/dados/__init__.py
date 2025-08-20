from mundo3.desafios.desafio115b import menu


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(menu.mostrar_erro('Por favor, digite um número inteiro válido'))
            continue
        except KeyboardInterrupt:
            print(menu.mostrar_erro('Usuário preferiu não digitar esse número'))
            return 0
        else:
            return n


def arquivo_existe(arquivo):
    try:
        arq = open(arquivo, 'rt')  # rt serve para ler arquivos de texto
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arquivo):
    try:
        arq = open(arquivo, 'wt+')  # wt serve para escrever arquivos de texto. O + é para criar caso não exista
        arq.close()
    except:
        print(menu.mostrar_erro(f'Não foi possível criar o arquivo {arquivo}'))
    else:
        print(menu.mostrar_sucesso(f'Arquivo {arquivo} criado com sucesso!'))


def ler_cadastro(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except:
        print(menu.mostrar_erro(f'Não foi possível ler o arquivo {arquivo}'))
    else:
        menu.titulo('PESSOAS CADASTRADAS')
        for linha in arq:
            linha_limpa = linha.strip()
            dados = linha_limpa.split(',')
            print(f'{dados[0]:<42}{dados[1]:>3} anos')
    finally:
        arq.close()


def cadastrar(arquivo):
    try:  # Tenta abrir o arquivo
        arq = open(arquivo, 'at')
    except:
        print(menu.mostrar_erro(f'Não foi possível abrir o arquivo {arquivo}'))
    else:
        try:  # Tenta iniciar o cadastro
            menu.titulo('NOVO CADASTRO')
            while True:
                try:  # Tenta validar os dados
                    nome = str(input('Nome: ')).strip().capitalize()
                    idade = leiaInt('Idade: ')
                except (ValueError, TypeError):
                    print(menu.mostrar_erro('Dados não validados'))
                else:
                    try:  # Tenta gravar os dados no arquivo
                        with open(arquivo, 'at') as arq:
                            arq.write(f'{nome},{idade}\n')
                    except:
                        print(menu.mostrar_erro(f'Não foi possível gravar registro no arquivo {arquivo}'))
                    else:
                        print(menu.mostrar_sucesso(f'Registro de {nome} adicionado com sucesso no arquivo {arquivo}'))
                finally:
                    break
        except:
            print(menu.mostrar_erro('Cadastro não realizado'))
    finally:
        arq.close()
