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
    return f'R$ {valor:>5.2f}'.replace('.',',')


def resumo(valor, aum=0, red=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<18} {moeda(valor)}')
    print(f'{"Dobro do preço:":<18} {dobro(valor, True)}')
    print(f'{"Metade do preço:":<18} {metade(valor, True)}')
    print(f'{f"{aum}% de aumento:":<18} {aumentar(valor, aum, True)}')
    print(f'{f"{red}% de redução:":<18} {diminuir(valor, red, True)}')
    print('-' * 30)
