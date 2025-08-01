palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    vogais = ' '
    for c in range(0, len(palavra)):
        if palavra[c] in 'aeiou':
            letra = palavra[c] + ' '
            vogais += letra
    print(f'Na palavra {palavra.upper()} temos as vogais: {vogais}')
