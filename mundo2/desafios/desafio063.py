print('-' * 60)
print(f'{" SEQUÊNCIA DE FIBONACCI ":@^60}')
print('-' * 60)

n1 = n2 = c = 1
n = int(input('Insira um número: '))
print('-' * 60)
print(f'Os {n} primeiros números da Sequência de Fibonacci são:')
print('-' * 60)
print(f'{n1} ➞ {n2}', end=' ➞ ')
while c < n - 1:
    n3 = n1 + n2
    print(n3, end=' ➞ ')
    n1 = n2
    n2 = n3
    c += 1
