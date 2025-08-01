listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 50)
print('{:^50}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 50)

for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{item:.<40}',end='')
    else:
        print(f'R$ {item:>7.2f}')
print('-' * 50)
