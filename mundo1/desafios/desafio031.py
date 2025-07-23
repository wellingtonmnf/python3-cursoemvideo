d = float(input('Digite a distância do percurso (km): '))

if d <= 200:
    print(f'O valor da passagem é R$ {(d*0.5):.2f}')
else:
    print(f'O valor da passagem é R$ {(d*0.45):.2f}')