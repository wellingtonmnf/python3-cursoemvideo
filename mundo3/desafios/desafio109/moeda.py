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
    return f'R$ {valor:.2f}'
