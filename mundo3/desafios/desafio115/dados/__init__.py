def cadastrar():
    print('-' * 50)
    print('NOVO CADASTRO'.center(50))
    print('-' * 50)
    while True:
        try:
            nome = str(input('Nome:')).strip().capitalize()
            idade = int(input('Idade: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido\033[m')
        else:
            with open('dados/pessoas.txt', 'a') as arquivo:
                arquivo.write(f'{nome},{idade}' + '\n')
            print(f'Registro de {nome} adicionado')
            break


def ler_cadastro():
    pessoas = []
    with open('dados/pessoas.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            dados = linha_limpa.split(',')
            pessoas.append(dados)

    print('-' * 50)
    print('PESSOAS CADASTRADAS'.center(50))
    print('-' * 50)
    for p in pessoas:
        print(f'{p[0]:<42}{p[1]:>3} anos')
