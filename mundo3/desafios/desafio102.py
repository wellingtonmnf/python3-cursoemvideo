def fatorial(n=1, show=False):
    """
    ≥ Calcula o fatorial de um número (n!)
    :param n: O número a ser calculado
    :param show: (Opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial de um número n (n!)
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if show == True:
            print(c, end=' ')
            if c != 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return fat


print(f'-' * 30)
print(fatorial(5, True))
print(fatorial(3))
print(fatorial(6, True))
print(fatorial())
help(fatorial)
