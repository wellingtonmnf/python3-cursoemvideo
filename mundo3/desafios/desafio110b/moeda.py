def aumentar(valor, porc, format=False):
    valor = valor + (valor * porc / 100)
    if format:
        valor = moeda(valor)
    return valor


def diminuir(valor, porc, format=False):
    valor = valor - (valor * porc / 100)
    if format:
        valor = moeda(valor)
    return valor
    return valor


def dobro(valor, format=False):
    valor *= 2
    if format:
        valor = moeda(valor)
    return valor


def metade(valor, format=False):
    valor /= 2
    if format:
        valor = moeda(valor)
    return valor


def moeda(valor):
    return f'R$ {valor:>5.2f}'


def titulo(msg, param=-1):
    if param > -1:
        return f'{f"{param}{msg}":<18}'
    else:
        return f'{msg:<18}'


def resumo(valor, aum=0, red=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{titulo('Preço analisado:')}R$ {valor:>5.2f}')
    print(f'{titulo('Dobro do preço:')}{dobro(valor, True)}')
    print(f'{titulo('Metade do preço:')}{metade(valor, True)}')
    print(f'{titulo('% de aumento:', aum)}{aumentar(valor, aum, True)}')
    print(f'{titulo('% de redução:', red)}{diminuir(valor, red, True)}')
    print('-' * 30)
