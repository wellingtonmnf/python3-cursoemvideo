def cabecalho():
    print('\033[7:32:40m~' * 27)
    print('\033[7:32:40mSISTEMA DE AJUDA PyHELP'.center(27))
    print('\033[7:32:40m~' * 27)
    print('\033[m', end='')


def acesso(param):
    print('\033[7:34:40m~' * 32)
    print(f"\033[7:34:40mAcessando o manual do comando '{param}'")
    print('\033[7:34:40m~' * 32)
    print('\033[m', end='')


def fim():
    print('\033[7:31:40m~' * 32)
    print(f'\033[7:31:40mATÉ LOGO!')
    print('\033[7:31:40m~' * 32)


def ajuda():
    while True:
        cabecalho()
        param = str(input('\033[mFunção ou Biblioteca > '))
        param.strip().lower()
        if param == 'fim':
            break
        acesso(param)
        print('\033[7m', end='')
        help(param)
    fim()

ajuda()
