from time import sleep

#DESAFIO PRÓPRIO:
# Transformar essa tupla em um dicionário passando a chave com o mode da configuração, ao invés de um código numérico

c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[0;30;46m',  # 6 - branco
     '\033[0;30;47m',  # 7 - cinza
     '\033[7m'  # 8 - invertido
     ) # Variável GLOBAL


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[8], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
