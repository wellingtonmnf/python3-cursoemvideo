from time import sleep

# DESAFIO PRÓPRIO:
# Transformar a tupla proposta pelo Guanabara em um dicionário passando a chave com o nome da cor, ao invés de um código numérico

cores = {'sem cor': '\033[m',
         'vermelho': '\033[0;30;41m',
         'verde': '\033[0;30;42m',
         'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m',
         'roxo': '\033[0;30;45m',
         'branco': '\033[0;30;46m',
         'cinza': '\033[0;30;47m',
         'invertido': '\033[7m'}


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 'azul')
    print(cores['invertido'], end='')
    help(com)
    print(cores['invertido'], end='')
    sleep(2)


def titulo(msg, cor='sem cor'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores['sem cor'], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 'vermelho')
