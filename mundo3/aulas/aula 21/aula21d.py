def somar(a=0, b=0, c=0): # definição de parâmetros opcionais
    # Declarados dessa forma, permitem que a função receba menos argumentos
    # do que o número total declarado de parâmetros
    """
    — > Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Gustavo Guanabara do canal Curso em Vídeo
    """
    s = a + b + c
    print(f'A soma vale {s}')


# somar(3, 2, 5, 8) # Não funciona, pois tem mais valores passados do que parâmetros definidos
somar(c =3, a = 2, b = 5)
somar(b = 3, c =2)
somar(3)
somar()

'''Quando possui um valor atribuído previamente, este parâmetro torna-se opcional'''
