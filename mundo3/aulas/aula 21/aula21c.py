def contador(i, f, p): # Criação de uma Docstring
    # Para criar uma Docstring, se coloca dentro do corpo da função (com indentação)
    # três aspas duplas para abrir o corpo da Docstring e mais três para fechar
    """
    ≥ Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal Curso em Vídeo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(2, 10, 2)
contador(0, 100, 10)

help(contador) # Exibe a Docstring criada
print(contador.__doc__)