frase = str(input('Digite uma frase: ')).upper().strip() # Tira os espaços de margem e coloca tudo em maiúscula
palavras = frase.split() # separa cada palavra pelos espaços internos e faz um array de palavras
junto = ''.join(palavras) # junta cada palavra com um espaço vazio, unificando a string sem espaços
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
