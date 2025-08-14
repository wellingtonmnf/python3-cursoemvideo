def aumentar(valor, porc):
    valor = valor + (valor * porc / 100)
    return valor


def diminuir(valor, porc):
    valor = valor - (valor * porc / 100)
    return valor


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor):
    return f'R$ {valor:.2f}'
