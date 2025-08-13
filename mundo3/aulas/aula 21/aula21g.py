def teste(b): # Parâmetro formal recebe AQUI a CÓPIA do valor de A
    a = 8 # Variável LOCAL que NÃO altera o valor de a GLOBAL
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # Variável GLOBAL que NÃO é afetada pela função
teste(a) # Parâmetro real
print(f'A fora vale {a}')
