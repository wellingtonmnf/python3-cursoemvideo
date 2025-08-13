def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a} m²')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
