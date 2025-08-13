def area(l, c):
    a = l * c
    print(f'A área de um terreno de {largura:.2f} x {comprimento:.2f} é de {a:.2f} m²')


print('Controle de Terrenos'.center(30))
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)
