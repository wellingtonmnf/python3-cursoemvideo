print('-' * 50)
print(f'{"PROGRESSÃO ARITMÉTICA":^^50}')
print('-' * 50)

a = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('-' * 30)

print(f'Os 10 primeiros termos da PA de {a} com razão {r} são:')
print(f'{a}...', end='')
pa = a
for c in range(1, 10):
    pa = pa + r
    print(f'{pa}...',end='')



