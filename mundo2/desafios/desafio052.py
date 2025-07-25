print('=' * 30)
print(f'{"CHECAGEM DE NÚMERO PRIMO":^30}')
print('=' * 30)

n = int(input('Informe um número: '))
validador = 0

if n <= 1:
    print(f'Número inválido!')
    print(f'Insira um número inteiro MAIOR que 1')
elif n == 2:
    print(f'{n} é um número PRIMO')
else:
    for c in range(2, n):
        if n % c == 0:
            validador += 1

    if validador == 0:
        print(f'{n} é um número PRIMO')
    else:
        print(f'{n} não é um número PRIMO')