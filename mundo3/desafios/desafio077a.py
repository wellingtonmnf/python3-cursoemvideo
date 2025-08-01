palavras = ('arroz', 'feijao', 'batata', 'cenoura', 'beterraba', 'cebola', 'pimentao')

for palavra in palavras:
    letras = ' '
    for letra in palavra:
        letra += ' '
        letras += letra
    letras = letras.split()
    # print(letras)
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
    vogais = ' '
    for letra in letras:
        if letra in 'aeiou':
            letra += ' '
            vogais += letra
    print(f'{vogais.upper()} ', end='')
    print()
