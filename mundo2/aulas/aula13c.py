for c in range(0, 3):
    print(f'Iteração nº {c}')

print('-' * 15)
for c in range(0, 10):
    print(f'Iteração nª {c}')
    c = c + 1 # Essa iteração não funciona. Pesquisar depois o motivo

print('-' * 15)
for c in range(0, 10):
    print(f'Iteração nº {c}')
    if c % 2 == 1:
        print(f'Iteração ímpar')
    print('Fim do ciclo')