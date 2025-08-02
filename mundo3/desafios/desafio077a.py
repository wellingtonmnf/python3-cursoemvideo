palavras = ('arroz', 'feijao', 'batata', 'cenoura', 'beterraba', 'cebola', 'pimentao')

for palavra in palavras:
    letras = ' '
    for letra in palavra:
        letra += ' '
        letras += letra
    letras = letras.split()
    # Separar cada letra desta forma funciona. Porém, strings já são listas de letras
    # este exercício foi feito assim apra tentar não usar nenhuma funcionalidade
    # de listas, já que este assunto ainda não havia sido estudado
    print(f'Na palavra {palavra.upper()} temos as vogais: ', end='')
    vogais = ' '
    for letra in letras:
        if letra in 'aeiou':
            letra += ' '
            vogais += letra
    print(f'{vogais.upper()}')
