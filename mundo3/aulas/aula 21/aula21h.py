def teste(b): # Parâmetro formal recebe AQUI a CÓPIA do valor de A
    global a # Aqui é dito apra a função usar a variável GLOBAL
    a = 8 # Variável GLOBAL que tem seu valor alterado
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # Variável GLOBAL que É afetada pela função
teste(a) # Parâmetro real
print(f'A fora vale {a}')
